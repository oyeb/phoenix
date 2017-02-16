from botapi import game
import sys

while True:
    game_state = game(input(), 'kevin')
    
    """
    ============================================================
    Fill with the moves that you have to make on each child
    ============================================================
    """

    print(game_state.make_move())
    sys.stdout.flush()
