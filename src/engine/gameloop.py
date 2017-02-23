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
    
def disqualify_bot(lst, position, reason=""):
    lst[position].write_to_log(reason)
    lst[position].game_over()
    lst.pop(position)

def kill_all(lst):
    map(lambda x: x.game_over(), lst)

def is_some_bot_alive(lst):
    return reduce(lambda x, y: x and y, map(lambda x: x.is_alive(), lst), False)

def initialize_bots(map_text, lst):
    prev_state = loads(map_text)

    prev_state['bots'] = list(map(lambda x : {'botname':x,
                                              'score':0,
                                              'angle':randint(0, 360),
                                              'velocity':0.59,
                                              'mass':20,
                                              'radius':10,
                                              'childno':0,
                                              'center':(randint(0, 4992), randint(0, 2808))}, lst))

    # The '\n' acts as RETURN after the raw_input()
    return dumps(prev_state)+'\n'

def gameloop(args, map_text, timeout, max_iters):
    """
    This is the game loop, it takes the moves, processes it, writes the new
    state to the medium (here pipe).
    """
    
    game = Gamectl()
    args = map(tuple, args)
    
    game_state_log = open('game_state_log.txt', 'w')
    gslog = []

    try:
        bots = [Botctl(name, arg) for name, arg in args]
    except Exception as e:
        print "I'm an exception: {}".format(e.message)
        
    prev_state = initialize_bots(map_text, [name for name, arg in args])

    for i in xrange(max_iters):
        update_and_suspend_all(bots, prev_state)
        
        moves = []
        for (bot, num) in zip(bots, xrange(len(bots))):
            bot.resume_bot()
            move = bot.get_move(timeout)
            print "{}'s move: {}".format(bot.name, move)
            bot.suspend_bot()
            if bot.is_alive() and game.is_valid_move(prev_state, move):
                moves.append((bot.name, move))
            else:
                disqualify_bot(bots,
                               num,
                               "Either the bot made an invalid move or time limit exceeded!\n")
        prev_state = game.next_state_continuous(prev_state, moves)
        gslog.append(prev_state)

    kill_all(bots)
    game_state_log.write('\n,'.join(gslog))
    
    print '='*80
    print 'Game Over'.center(80)
    print '='*80
