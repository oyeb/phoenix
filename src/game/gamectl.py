import os
from json import loads, dumps
from jsonschema import Draft4Validator
from vividict import vividict

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
        Moves made are in the following order:
        direction > split > eject > decay-operation > update-radius > update-velocity-wrt-mass > pause > run-game-for-100-ticks
        """

        cur_state = loads(prev_state)
        bots = vividict()
        for child in cur_state['bots']:
            bots[child['botname']][child['childno'])] = child

        for name, moves in bot_move_list:
            for move in moves:
                childno = move['childno']

                # direction operation
                bots[name][childno]['angle'] += move['relativeangle']
                bots[name][childno]['angle'] %= 360

                # Split takes place here [NOT IMPLEMENTED]

                # eject mass operation
                if move['ejectmass'] and bots[name][childno][mass] >= 20:
                    bots[name][childno]['mass'] -= 2

                # decay operation
                bots[name][childno]['mass'] -= 0.002*bots[name][childno]['mass']

                # update radius
                bots[name][childno]['radius'] = bots[name][childno]['mass']/2.0

                # update velocity with respect to mass
                bots[name][childno]['velocity'] = 2.2*(bots[name][childno][mass]**-0.439)

                # pause operation
                if move['pause']:
                    bots[name][childno]['velocity'] = 0

                # run game for 100 ticks
