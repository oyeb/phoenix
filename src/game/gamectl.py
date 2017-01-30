class Gamectl:
    def is_valid_move(self, bot_move):
        """Validates the move made by a bot."""

        if bot_move == None:
            return False
        else:
            # This is for testing purpose
            return True
    def next_state_continuous(self, prev_state, bot_move_list):
        """
        Creates a new game-state from the previous state and the new moves made
        by the bots.
        """

        # This is for testing purpose
        return prev_state
