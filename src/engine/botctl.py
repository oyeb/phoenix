import os
from signal import SIGCONT, SIGSTOP, SIGTERM
from time import sleep
import sys

class BotState:
    active = 0
    suspended = 1
    busy = 2
    unresponsive = 3
    disqualified = 4

# defined as sky
class Botctl:
    def __init__(self, timeout=0.2, args):
        """args should be a list,
        example: ['/usr/bin/python', 'python', 'bot1.py']"""

        self.BOTIN_CHILD, self.BOTIN_PARENT = os.pipe()
        self.BOTOUT_PARENT, self.BOTOUT_CHILD = os.pipe()

        # the stderr is redirected here and logged
        self.bot_err_log = open('bot_err_log.txt', 'w')

        self.moves = []
        self.bot_status = BotState.active
        self.bot_pid = os.fork()
        
        if self.bot_pid == 0:
            os.close(self.BOTIN_PARENT)
            os.close(self.BOTOUT_PARENT)

            os.dup2(self.BOTIN_CHILD, sys.stdin.fileno())
            os.dup2(self.BOTOUT_CHILD, sys.stdout.fileno())
            os.dup2(self.bot_err_log.fileno(), sys.stderr.fileno())

            self.bot_err_log.close()

            # seccomp filter
            # memory management
            execl(*args)
        else:
            os.close(self.BOTIN_CHILD)
            os.close(self.BOTOUT_CHILD)
            self.bot_err_log.close()
            
            self.botin = fdopen(self.BOTIN_PARENT, 'w')
            self.botout = fdopen(self.BOTOUT_PARENT, 'r')
            self.bot_move_log = open('bot_move_log.txt', 'w')

            sleep(timeout)

            if self.get_move() == "I'm Poppy!":
                print "Bot acknowledged"
            else:
                self.bot_status = BotState.unresponsive
                print "Bot unresponsive"
                self.game_over()

    def suspend_bot(self):
        os.kill(self.bot_pid, SIGSTOP)

    def resume_bot(self):
        os.kill(self.bot_pid, SIGCONT)

    def kill_bot(self):
        os.kill(self.bot_pid, SIGTERM)

    def get_move(self):
        move =  self.botout.read()
        self.moves.append(move)
        return move

    def update_game_state(self, new_state):
        """new_state is a sting"""
        self.botin.write(new_state)

    def append_logs(self):
        self.bot_move_log.write('\n'.join(moves))
        self.bot_move_log.close()

    def game_over(self):
        self.botin.close()
        self.botout.close()
        self.append_logs()
        self.kill_bot()
