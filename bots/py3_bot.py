from botapi import game
import sys

game.send_acknowledgement()

while True:
    game_state = game('joker')
    
    """
    ============================================================
    Fill with the moves that you have to make on each child
    ============================================================
    """
    
    game_state.send_move()
