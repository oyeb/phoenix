from botapi import game
import sys

print "I'm Poppy!"
sys.stdout.flush()

i = 0
while True:
    gs_json = raw_input()
    game_state = game(gs_json, 'kevin')
    sys.stderr.write("Iter no: {}".format(i))
    i+=1
    
    """
    ============================================================
    Fill with the moves that you have to make on each child
    ============================================================
    """
    
    print game_state.make_move()
    sys.stdout.flush()
