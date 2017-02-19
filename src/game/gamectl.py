import os
from json import loads, dumps
from jsonschema import Draft4Validator
from vividict import vividict
from copy import deepcopy
from math import sin, cos, radians

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

    def genchild(self, nums):
        """
        Return a new unique number for childno of new bot created through split
        """
        return max(nums)+1

    def next_state_continuous(self, prev_state, bot_move_list):
        """
        Creates a new game-state from the previous state and the new moves made
        by the bots.
        Moves made are in the following order:
        direction > decay-operation > eject-mass > update-velocity-wrt-mass > pause > split > upd-rad-wrt-mass > run-the-move
        2, 3 are mass ops
        4, 5 are velocity ops
        6 is mass, velocity op
        7 is radius op
        """
        
        cur_state = loads(prev_state)
        moves_all = map(lambda (x, y): (x, loads(y)), bot_move_list)
        
        bots = vividict()
        for child in cur_state['bots']:
            bots[child['botname']][child['childno']] = child

        for name, moves in moves_all:
            for move in moves:
                childno = move['childno']

                # direction operation
                bots[name][childno]['angle'] += move['relativeangle']
                bots[name][childno]['angle'] %= 360
                ejectangle = (180.0 + bots[name][childno]['angle']) % 360

                # decay operation
                bots[name][childno]['mass'] -= 0.002*bots[name][childno]['mass']

                # eject mass operation
                if move['ejectmass'] and bots[name][childno][mass] >= 20.0:
                    bots[name][childno]['mass'] -= 2
                    ejectx = bots[name][childno]['Xcoordinate'] - (bots[name][childno]['radius'] + 50)*cos(radians(ejectangle))
                    ejecty = bots[name][childno]['Ycoordinate'] - (bots[name][childno]['radius'] + 50)*sin(radians(ejectangle))
                    cur_state['food'].append((ejectx, ejecty))

                # update velocity with respect to mass
                bots[name][childno]['velocity'] = 2.2*(bots[name][childno]['mass']**-0.439)

                # pause operation
                if move['pause']:
                    bots[name][childno]['velocity'] = 0         

                # Split operation
                if bots[name][childno]['mass'] >= 36.0 and len(moves) < 16:
                    newchildno = self.genchild(bots[name].keys())
                    bots[name][newchildno] = deepcopy(bots[name][childno])
                    
                    bots[name][childno]['mass'] /= 2.0
                    bots[name][childno]['velocity'] = 0.70 # revise this velocity
                    bots[name][childno]['angle'] = ejectangle
                    
                    bots[name][newchildno]['mass'] /= 2.0
                    bots[name][newchildno]['velocity'] /= 0.70 # revise this velocity
                
                # update radius
                bots[name][childno]['radius'] = bots[name][childno]['mass']/2.0

                # run-game [NOT IMPLEMENTED]

        # this \n acts like the RETURN key pressed after entering the input
        # [IMPLEMENT EXCEPTION HANDLING HERE IF THERE WAS NO '\n']
        return dumps(cur_state)+'\n'
