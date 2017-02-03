from botapi import game
from json import loads, dumps
import sys

while True:
    game_state = game(sys.stdin.read(), 'kevin')
    
    """
    ============================================================
    Fill with the moves that you have to make on each child
    ============================================================
    """

    print dumps(game_state.get_children(), sort_keys=True, indent=4)
    print game_state.make_move()
    sys.stdout.flush()
    break
