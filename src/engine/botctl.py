# This file is part of Phoenix
#
# Copyright (c) 2016, 2017 Vasantha Ganesh K.
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with is source code.

import os
from signal import SIGCONT, SIGSTOP, SIGTERM, SIGINT
from time import sleep
from resource import setrlimit, RLIMIT_AS
import sys
from syscall_filter import syscall_filter
from random import randint
import fcntl
from select import select

# fcntl constant for setting the pipe size. Linux only feature. Not available on
# other unix os. To use it in C, use `#define _GNU_SOURCE` before #include
# statements.
fcntl.F_SETPIPE_SZ = 1031

class BotState:
    """Bot process status. Decided by the Engine."""
    active = 0
    suspended = 1
    busy = 2
    unresponsive = 3
    disqualified = 4

# defined as sky
class Botctl:
    def __init__(self, name, args, timeout=2.0, mem_limit=10**9):
        """Launches the bot process. timeout (seconds, float accepted) is the 
        time for which the engine waits for the bot to acknowledge i.e. send
        "I'm Poppy!" in the medium (anonymous pipe here). args should be a list,
        example: ['/usr/bin/python', 'python', 'bot1.py'] this will be 
        directly executed with execlp. mem_limit is the memory limit in bytes. 
        It also initiates the seccomp-bpf filter to restrict the system calls
        that can be used by the bot. Resources such as stack and heap or the
        whole memory is given an upper limit here. We also pipe the STDIN and
        STDOUT of the bot to some file that can be manipulated by the engine.
        """

        # Hard coded pipe size
        self.PIPESZ = 8192

        self.name = name
        self.valid = False

        self.BOTIN_CHILD, self.BOTIN_PARENT = os.pipe()
        self.BOTOUT_PARENT, self.BOTOUT_CHILD = os.pipe()

        # Increse the pipe buffer size to 8 MB
        fcntl.fcntl(self.BOTOUT_CHILD, fcntl.F_SETPIPE_SZ, self.PIPESZ)
        fcntl.fcntl(self.BOTOUT_PARENT, fcntl.F_SETPIPE_SZ, self.PIPESZ)
        fcntl.fcntl(self.BOTIN_CHILD, fcntl.F_SETPIPE_SZ, self.PIPESZ)
        fcntl.fcntl(self.BOTIN_PARENT, fcntl.F_SETPIPE_SZ, self.PIPESZ)

        # the stderr is redirected here and logged
        self.bot_err_log = open('bot_err_log{}.txt'.format(self.name), 'w')

        self.moves = []
        self.bot_status = BotState.active
        self.bot_pid = os.fork()
        
        if self.bot_pid == 0:
            # seccomp filter
            syscall_filter()

            os.close(self.BOTIN_PARENT)
            os.close(self.BOTOUT_PARENT)

            os.dup2(self.BOTIN_CHILD, sys.stdin.fileno())
            os.dup2(self.BOTOUT_CHILD, sys.stdout.fileno())
            os.dup2(self.bot_err_log.fileno(), sys.stderr.fileno())

            self.bot_err_log.close()            
            
            # This lime sets 1 GiB of memory per process. It limits the whole
            # memory, but limiting stack and heap size is not done explicitly.
            setrlimit(RLIMIT_AS, (mem_limit, mem_limit))
            
            os.execl(*args)
        else:
            os.close(self.BOTIN_CHILD)
            os.close(self.BOTOUT_CHILD)
            self.bot_err_log.close()

            flg = fcntl.fcntl(self.BOTOUT_PARENT, fcntl.F_GETFL)
            fcntl.fcntl(self.BOTOUT_PARENT, fcntl.F_SETFL, flg | os.O_NONBLOCK) 
            
            self.botin = os.fdopen(self.BOTIN_PARENT, 'w')
            self.bot_move_log = open('bot_move_log{}.txt'.format(self.name), 'w')

            # enables non blocking read on the bot's stdin so that the engine can read
            # whenever it wants.

            if self.get_move(2.0) == "I'm Poppy!":
                self.valid = True
                print "[*] {} has been acknowledged.".format(self.name)
            else:
                print "[*] {} is unresponsive".format(self.name)
                # self.game_over()

    def suspend_bot(self):
        """ Suspends the bot process (if currently active)."""

        self.bot_status = BotState.suspended
        os.kill(self.bot_pid, SIGSTOP)

    def resume_bot(self):
        """Resumes the bot process (if suspended earlier)."""

        self.bot_status = BotState.active
        os.kill(self.bot_pid, SIGCONT)

    def kill_bot(self):
        """ Kills the bot process."""

        if self.is_alive():
            os.kill(self.bot_pid, SIGTERM)

    def is_alive(self):
        """Check for the existence of unix pid."""
        try:
            os.kill(self.bot_pid, 0)
        except OSError:
            return False
        else:
            return True

    def write_to_log(self, reason=""):
        self.moves.append(reason)

    def get_move(self, timeout):
        """Requests bot to compute a move and write a JSON_OBJ to the medium. The 
        process is then suspended (not necessarily explicitly). If a valid move is
        not found on the medium within timeout seconds, the bot forgoes this "turn"
        and is suspended. A (penalty or invalid-move) is awarded if move is invalid
        or incomplete. A (penalty or no-move) is awarded is medium is found empty.
        """

        ready, _, _ = select([self.BOTOUT_PARENT], [], [], timeout)
        if len(ready) == 1:
            move =  os.read(self.BOTOUT_PARENT, self.PIPESZ).strip()
        else:
            move = None
            
        self.moves.append(move)
        return move

    def update_game_state(self, new_state):
        """new_state is a sting. The engine sends the new_state (of the game) to
        the bot via the medium. This new_state was procured (and is forwarded)
        from the game when moves of (turn number - 1) were executed by the game.
        This need not be a JSON object as it is game-dependent. Expects bot
        process to acknowledge receipt by writing to the medium."""
        
        self.botin.write(new_state)
        self.botin.flush()

    def append_logs(self):
        """logs is a container (list) of various log-channels like info-from-game,
        move-errors, etc. that were generated by the game while executing (turn number)
        moves."""

        self.moves = map(lambda x: '' if x == None else x, self.moves)
        self.bot_move_log.write('\n'.join(self.moves))

    def game_over(self):
        """When a bot is unable to make a move it is said to be "defeated".
        Engine inspects the game-state at each turn to kill bots that have
        been "defeated". Engine appends a game-summary to the logs (when 
        append_logs) is called. Also closes all the file descriptors."""

        print '[*] {} died!'.format(self.name)
        
        self.append_logs()
        self.bot_move_log.close()

        self.kill_bot()
        os.close(self.BOTOUT_PARENT)
        self.botin.close()
