from botapi import game
import sys

print "I'm Poppy!"
sys.stdout.flush()

while True:
    gs_json = raw_input()
    # game_state = game(gs_json, 'kevin')
    
    """
    ============================================================
    Fill with the moves that you have to make on each child
    ============================================================
    """
    
    # print game_state.make_move()
    print gs_json
    sys.stdout.flush()
