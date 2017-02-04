import os
from json import loads, dumps
from jsonschema import Draft4Validator

class Gamectl:
    def is_valid_move(self, prev_state, bot_move):
        """Validates the move made by a bot."""

        cdir = os.path.dirname(os.path.realpath('__file__'))
        move_schema = open(os.path.join(cdir, 'src', 'game', 'moveschema.json'), 'r').read()
        
        try:
            move = loads(bot_move)
            game_state = loads(prev_state)
            Draft4Validator(loads(move_schema)).validate(move)
        except Exception as e:
            print "I'm the exception: {}".format(e.message)
            return False
        else:
            chld_prev_state = sorted(set(list(map(lambda x: x['childno'], game_state['bots']))))
            chld_move = sorted(list(map(lambda x: x['childno'], move)))
            if chld_move == chld_prev_state:
                return True
            else:
                return False

    def next_state_continuous(self, prev_state, bot_move_list):
        """
        Creates a new game-state from the previous state and the new moves made
        by the bots.
        """

        # This is for testing purpose
        return prev_state
