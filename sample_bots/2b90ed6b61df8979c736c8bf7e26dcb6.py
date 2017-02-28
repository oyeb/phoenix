from botapi import game

game.send_acknowledgement()

while True:
    game_state = game('py2_bot')
    
    """
    ============================================================
    Fill with the game logic that you have to make on each child
    ============================================================
    """
    
    game_state.send_move()
