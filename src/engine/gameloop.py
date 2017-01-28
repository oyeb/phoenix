# This file is part of Phoenix
#
# Copyright (c) 2016, 2017 Vasantha Ganesh K.
#
# For the full copyright and license information, please view the LICENSE file
# that was distributed with is source code.

from botctl import Botctl
from game.gamectl import Gamectl
from time import sleep

def suspend_all(lst):
    map(lambda x: x.suspend_bot(), lst)

def resume_all(lst):
    map(lambda x: x.resume_bot(), lst)

def update_all(lst, new_state):
    map(lambda x: x.update_game_state(new_state), lst)
    
def disqualify_bot(lst, position, reason=""):
    lst[position].write_to_log(reason)
    lst[position].game_over()
    lst.pop(position)

def kill_all(lst):
    map(lambda x: x.game_over(), lst)

def is_some_bot_alive(lst):
    return reduce(lambda x, y: x and y, map(lambda x: x.is_alive(), lst))
    
def gameloop(args, map_text):
    """
    This is the game loop, it takes the moves, processes it, writes the new
    state to the medium (here pipe).
    """
    
    game = Gamectl()
    prev_state = map_text
    bots = [Botctl(i) for i in args]

    while is_some_bot_alive(bots):
        print "I'm into gameloop"
        update_all(bots, prev_state)
        suspend_all(bots)
        
        moves = []
        for (bot, num) in zip(bots, xrange(len(bots))):
            bot.resume_bot()
            sleep(1.0)
            if bot.is_alive():
                moves.append(bot.get_move())
                bot.suspend_bot()
            else:
                disqualify_bot(bots, num, "The bot died unfortunately!\n")

        valid_moves = []
        for (move, num) in zip(moves, xrange(len(bots))):
            if game.is_valid_move(move):
                valid_moves.append(move)
            else:
                disqualify_bot(bots, num, "The bot made an invalid move!\n")

        prev_state = game.next_state_continuous(prev_state, valid_moves)
        break

    kill_all(bots)
