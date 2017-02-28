# This file is part of Phoenix
#
# Copyright (c) 2016, 2017 Vasantha Ganesh K.
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with is source code.

from botctl import Botctl
from game.gamectl import Gamectl
from time import sleep
from json import loads, dumps
from random import randint
from tqdm import tqdm
import os.path, shutil

def suspend_all(lst):
    map(lambda x: x.suspend_bot(), lst)

def resume_all(lst):
    map(lambda x: x.resume_bot(), lst)
    
def update_and_suspend_all(lst, new_state):
    def update_and_suspend(x, new_state):
        x.resume_bot()
        x.update_game_state(new_state)
        x.suspend_bot()
        
    map(lambda x: update_and_suspend(x, new_state), lst)
    
def qualified_bots(lst):
    kill_all(filter(lambda x: not(x.valid), lst))
    return filter(lambda x: x.valid, lst)

def kill_all(lst):
    map(lambda x: x.game_over(), lst)

def kill_by_names(names_bot, lst):
    '''
    this method allows the game to kill a bot. This method should also log to
    the err_log
    '''
    
    for bot in lst:
        for name_bot in names_bot:
            if bot.name == name_bot:
                bot.valid = False

def is_some_bot_alive(lst):
    return reduce(lambda x, y: x and y, map(lambda x: x.is_alive(), lst), False)

def check_config(bots, mapfile, arena, commit_paths, api_dir):
    if not os.path.isdir(api_dir):
        raise Exception("Bad configuration, check path to %s" % api_dir)
    for key in commit_paths:
        commit_path = commit_paths[key]
        if not os.path.isdir(commit_path):
            raise Exception("Bad configuration, check path to %s" % commit_path)
    for bot in bots:
        if not os.path.exists(bot[1][2]):
            raise Exception("Bad configuration, check path to source code of '%s'\n%s." % (bot[0], bot[1][2]))
    if not os.path.exists(mapfile):
        raise Exception("Bad configuration, check path to mapfile '%s'." % mapfile)

def setup_arena(arena, bots, api_dir):
    shutil.rmtree(os.path.join(arena, 'logs'), ignore_errors=True)
    shutil.rmtree(os.path.join(arena, 'bots'), ignore_errors=True)
    os.mkdir(os.path.join(arena, 'logs'))
    os.mkdir(os.path.join(arena, 'bots'))
    for bot in bots:
        shutil.copytree(
            os.path.join(api_dir, bot[1][1]),
            os.path.join(arena, 'bots', bot[0])
        )
        shutil.copyfile(bot[1][2], os.path.join(arena, 'bots', bot[0], 'src', '__main__.py'))

def commit(bots, logfolder, filenames, commit_paths):
    err_log = {}
    dbg_log = {}
    mov_log = {}
    for bot in bots:
        err_log[bot.name] = open(os.path.join(logfolder, 'error_{0}'.format(bot.name)), 'r').read().strip().split('\n')
        dbg_log[bot.name] = open(os.path.join(logfolder, 'debug_{0}'.format(bot.name)), 'r').read().strip().split('\n')
        mov_log[bot.name] = open(os.path.join(logfolder, 'move_{0}'.format(bot.name)), 'r').read().strip().split('\n')

    elog = open(os.path.join(commit_paths['error'], filenames['error']), 'w')
    elog.write(dumps(err_log, indent=2))
    elog.close()
    dlog = open(os.path.join(commit_paths['debug'], filenames['debug']), 'w')
    dlog.write(dumps(dbg_log, indent=2))
    dlog.close()
    mlog = open(os.path.join(commit_paths['move'], filenames['move']), 'w')
    mlog.write(dumps(mov_log, indent=2))
    mlog.close()
    # move replay
    shutil.copyfile(
        os.path.join(logfolder, 'replay'),
        os.path.join(commit_paths['replay'], filenames['replay'])
    )

def gameloop(bots, mapfile, timeout, max_iters, arena, commit_paths, filenames, move_schema_path):
    """
    This is the game loop, it takes the moves, processes it, writes the new
    state to the medium (here pipe).
    """
    logfolder = os.path.join(arena, 'logs')
    # need to use paths inside the arena. bot_args is same as args(of code
    # before) and bots, except that the path is changed
    bot_args = [
    (
        bot[0],
        [
            bot[1][0],
            bot[1][1],
            os.path.join(arena, 'bots', bot[0], 'src').encode()
        ]
    ) for bot in bots]

    try:
        game = Gamectl(move_schema_path)
        args = map(tuple, bot_args)

        gslog = []
        
        bots = [Botctl(name, arg, logfolder) for name, arg in args]
        bots = qualified_bots(bots)

        map_text = open(mapfile, 'r').read().strip()
        prev_state = game.initialize_bots(map_text, [name for name, arg in args])
        
        for iteration in tqdm(xrange(max_iters)):
            update_and_suspend_all(bots, prev_state)
            
            moves = []
            for (bot, num) in zip(bots, xrange(len(bots))):
                bot.resume_bot()
                move = bot.get_move(timeout)
                bot.suspend_bot()
                
                if bot.is_alive() and game.is_valid_move(prev_state, move):
                    moves.append((bot.name, move))
                else:
                    bot.valid = False
            prev_state, to_kill = game.next_state_continuous(prev_state, moves)
            kill_by_names(to_kill, bots)
            gslog.append(prev_state)
                    
            bots = qualified_bots(bots)

    except Exception as e:
        print '[*] Exception: {}'.format(e)

    finally:
        kill_all(bots)
        # Will merge and move all logs from the arena, basically making it free
        # again.
        game_state_log = open(os.path.join(logfolder, 'replay'), 'w')
        game_state_log.write("var ob = [")
        game_state_log.write(',\n'.join(gslog))
        game_state_log.write("];")
        game_state_log.close()

        commit(bots, logfolder, filenames, commit_paths)
        summary = {
            'scores' : game.score,
            'iters' : iteration
        }
        with open(os.path.join(logfolder, "summary.json"), 'w') as summary_log:
            summary_log.write(dumps(summary))
