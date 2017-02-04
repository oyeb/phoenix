from botapi import game
from json import loads, dumps
import sys

print "I'm Poppy!"
sys.stdout.flush()

while True:
    gs_json = raw_input()
    game_state = game(gs_json, 'kevin')
    
    """
    ============================================================
    Fill with the moves that you have to make on each child
    ============================================================
    """
    
    print game_state.make_move()
    sys.stdout.flush()
