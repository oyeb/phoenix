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

def is_some_bot_alive(lst):
    return reduce(lambda x, y: x and y, map(lambda x: x.is_alive(), lst), False)

def gameloop(args, map_text, timeout, max_iters):
    """
    This is the game loop, it takes the moves, processes it, writes the new
    state to the medium (here pipe).
    """
    
    try:
        game = Gamectl()
        args = map(tuple, args)
        
        game_state_log = open('game_state_log.txt', 'w')
        score_log = open('score_log.txt', 'w')
        gslog = []
        
        bots = [Botctl(name, arg) for name, arg in args]
        bots = qualified_bots(bots)
                        
        prev_state = game.initialize_bots(map_text, [name for name, arg in args])
        
        for i in tqdm(xrange(max_iters)):
            if len(bots) <= 1:
                break
            
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
            prev_state = game.next_state_continuous(prev_state, moves)
            gslog.append(prev_state)
                    
            bots = qualified_bots(bots)

    except Exception as e:
        print '[*] Exception: {}'.format(e.message)

    finally:
        kill_all(bots)
        game_state_log.write('\n,'.join(gslog))
        score_log.write(dumps(game.score, indent=4))

        game_state_log.close()
        score_log.close()
    
        print '='*80
        print 'Game Over'.center(80)
        print '='*80
