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

    def update_position(self, tick_time, bot):
        bot['Xcoordinate'] -= bot['velocity']*tick_time*cos(radians(bot['angle']))
        bot['Ycoordinate'] -= bot['velocity']*tick_time*sin(radians(bot['angle']))

    def update_decay(self, bot):
        bot['mass'] -= 0.002*bot['mass']

    def update_direction(self, bot, rel_angle):
        bot['angle'] = (rel_angle + bot['angle']) % 360

    def update_velocity(self, bot):
        """
        Update velocity with respect to mass
        """
        bot['velocity'] = 2.2*(bot['mass']**-0.439)

    def update_radius(self, bot):
        """
        Update radius with respect to mass
        """
        bot['radius'] = bot['mass']/2.0

    def pause(self, bot):
        """
        Bring this particular child to halt
        """
        bot['velocity'] = 0
        

    def eject_mass(self, bot):
        ejectangle = (bot['angle'] + 180) % 360
        bots[name][childno]['mass'] -= 2
        ejectx = bot['Xcoordinate'] - (bot['radius'] + 50)*cos(radians(ejectangle))
        ejecty = bot['Ycoordinate'] - (bot['radius'] + 50)*sin(radians(ejectangle))
        return (ejectx, ejecty)
            
    def genchild(self, nums):
        """
        Return a new unique number for childno of new bot created through split
        """
        return max(nums)+1

    def split(self, bot, newchildno, tick_time):
        nbot = deepcopy(bot)
        ejectangle = (bot['angle'] + 180) % 360
        
        bot['mass'] /= 2.0
        bot['radius'] /= 2.0
        bot['velocity'] = (700 + 2*bot['radius'])/tick_time
        bot['angle'] = ejectangle

        nbot['childno'] = newchildno
        nbot['mass'] = bot['mass']
        nbot['radius'] = bot['radius']
        nbot['velocity'] = bot['velocity']

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
        ticks = 5
        tick_time = 20
        
        bots = vividict()
        for child in cur_state['bots']:
            bots[child['botname']][child['childno']] = child

        for name, moves in moves_all:
            for move in moves:
                childno = move['childno']
                bot = bots[name][childno]

                self.update_direction(bot, move['relativeangle'])
                self.update_decay(bot)

                if move['ejectmass'] and bot['mass'] >= 20.0:
                    cur_state['food'].append(self.eject_mass(bot))

                self.update_velocity(bot)
                if move['pause']:
                    self.pause(bot)

                if bot['mass'] >= 36.0 and len(moves) < 16 and move['split']:
                    newchildno = self.genchild(bots[name].keys())
                    cur_state['bots'].append(self.split(bot, newchildno, tick_time))
                
                self.update_radius(bot)

                for i in xrange(ticks):
                    map(lambda x : self.update_position(tick_time, x), cur_state['bots'])
                    # check collisions with food, cells, virus etc
                    map(lambda x : self.update_decay(x), cur_state['bots'])
                    map(lambda x : self.update_radius(x), cur_state['bots'])
                    map(lambda x : self.update_velocity(x), cur_state['bots'])
                
        # this \n acts like the RETURN key pressed after entering the input
        # [IMPLEMENT EXCEPTION HANDLING HERE IF THERE WAS NO '\n']
        return dumps(cur_state)+'\n'
