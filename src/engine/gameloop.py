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
    
def update_and_suspend_all(lst, new_state):
    def update_and_suspend(x, new_state):
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
    
def gameloop(args, map_text):
    """
    This is the game loop, it takes the moves, processes it, writes the new
    state to the medium (here pipe).
    """
    
    game = Gamectl()
    prev_state = map_text
    bots = [Botctl(i) for i in args]

    while is_some_bot_alive(bots):
        update_and_suspend_all(bots, prev_state)
        
        moves = []
        for (bot, num) in zip(bots, xrange(len(bots))):
            bot.resume_bot()
            sleep(2.0)
            bot.suspend_bot()
            
            move = bot.get_move().strip()
            if bot.is_alive() and game.is_valid_move(move):
                moves.append(move)
            else:
                disqualify_bot(bots,
                               num,
                               "Either the bot made an invalid move or time limit exceeded!\n")
            bot.suspend_bot()

        prev_state = game.next_state_continuous(prev_state, moves)

    print 'Out of gameloop'
