import os
import collisions
from json import loads, dumps
from jsonschema import Draft4Validator
from vividict import vividict
from copy import deepcopy
from math import sin, cos, radians
from random import randint

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
            print "[*] Exception: {}".format(e.message)
            return False
        else:
            chld_prev_state = sorted(set(list(map(lambda x: x['childno'], game_state['bots']))))
            chld_move = sorted(list(map(lambda x: x['childno'], move)))
            if chld_move == chld_prev_state:
                return True
            else:
                return False

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
        ejectx = bot['center'][0] - (bot['radius'] + 50)*cos(radians(ejectangle))
        ejecty = bot['center'][1] - (bot['radius'] + 50)*sin(radians(ejectangle))
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

    def colls_entities(self, bots, entity, rad):
        '''
        return a list of (time, 'entity_type', bot, entity_coordinates)
        '''
        etype = 'food' if rad == 2 else 'virus'
        
        collse = []
        for i in entity:
            for j in bots:
                collse.append((collisions.collision_bot_static_entity(j, i, rad), (j, i)))

        collse = filter(lambda ((a, b), (c, d)): a, collse)
        return [(b, etype, c, d) for ((a, b),(c, d)) in collse]

    def colls_bots(self, bots):
        '''
        return a list of (time, 'bot', bot, bot)
        '''
        
        collsb = []
        for i in range(len(bots)):
            for j in range(len(bots)):
                if i < j:
                    a, b = collisions.collision_bots_dynamic(bots[i], bots[j])
                    if a:
                        collsb.append(b, 'bot', bots[i], bots[j])
        return collsb

    def perform_collisions(self, dets):
        bots = []
        for bname in dets.keys():
            if bname != 'virus' and bname != 'food':
                bots.extend(dets[bname].values())

        colls = self.colls_entities(bots, dets['food'].keys(), 2)
        colls.extend(self.colls_entities(bots, dets['virus'].keys(), 35))
        colls.extend(self.colls_bots(bots))
        colls.sort()

        for (t, etype, bt, entity) in colls:
            bname = bt['botname']

            if bt['childno'] in dets[bname]:
                child = dets[bname][bt['childno']]
                
                if etype == 'virus' and tuple(entity) in dets['virus']:
                    if len(dets[bname].keys()) == 16:
                        child['mass'] += 70
                        child['score'] += 70*3
                    else:
                        newchild = self.genchild(dets[bt['botname']].keys())
                        dets[bname][newchild] = deepcopy(child)
                        child['mass'] /= 2.0
                        dets[bname][newchild]['mass'] /= 2.0
                    del dets['virus'][tuple(entity)]
                    
                elif etype == 'food' and tuple(entity) in dets['food']:
                    child['mass'] += 2
                    del dets['food'][tuple(entity)]
                    
                elif etype == 'bot' and entity['childno'] in dets[entity['botname']]:
                    bota, botb = child, dets[entity['botname']][entity['childno']]
                    bota, botb = (bota, botb) if bota['radius'] > botb['radius'] else (botb, bota)
                    
                    if bota['botname'] == botb['botname']:
                        bota[score] += botb['score']
                    else:
                        bota['mass'] += botb['mass']
                        bota['score'] += 10*botb['mass']    
                    del botb

                    
    def add_virus_food(self, dets, cnt_virus, cnt_food):
        for i in range(cnt_virus):
            dets['virus'][(randint(0, 4992), randint(0, 2808))] = None
        for i in range(cnt_food):
            dets['food'][(randint(0, 4992), randint(0, 2808))] = None

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
        tick_time = 20
        
        dets = vividict()
        for child in cur_state['bots']:
            dets[child['botname']][child['childno']] = child
        for virus in cur_state['virus']:
            dets['virus'][tuple(virus)] = None
        for food in cur_state['food']:
            dets['food'][tuple(food)] = None

        for name, moves in moves_all:
            for move in moves:
                childno = move['childno']
                bot = dets[name][childno]

                self.update_direction(bot, move['relativeangle'])
                self.update_decay(bot)

                if move['ejectmass'] and bot['mass'] >= 20.0:
                    dets['food'][self.eject_mass(bot)] = None

                self.update_velocity(bot)
                if move['pause']:
                    self.pause(bot)

                if bot['mass'] >= 36.0 and len(moves) < 16 and move['split']:
                    newchildno = self.genchild(bots[name].keys())
                    dets[name][newchildno] = self.split(bot, newchildno, tick_time)
                
                self.update_radius(bot)

                ##########
                #DEBUG THIS
                food_cnt = len(dets['food'].keys())
                virus_cnt = len(dets['virus'].keys())
                
                self.perform_collisions(dets)

                self.add_virus_food(dets, virus_cnt - len(dets['virus'].keys()), food_cnt - len(dets['food'].keys()))

                processed_bots = []
                for bname in dets.keys():
                    if bname != 'virus' and bname != 'food':
                        processed_bots.extend(dets[bname].values())
                processed_food = dets['food'].keys()
                processed_virus= dets['virus'].keys()

                cur_state['bots'] = processed_bots
                cur_state['virus'] = processed_virus
                cur_state['food'] = processed_food
                # END OF DEBUG THIS
                ##########

                map(lambda x : collisions.update_position(tick_time, x), cur_state['bots'])
                map(lambda x : self.update_velocity(x), cur_state['bots'])
                map(lambda x : self.update_radius(x), cur_state['bots'])

        # this \n acts like the RETURN key pressed after entering the input
        # [IMPLEMENT EXCEPTION HANDLING HERE IF THERE WAS NO '\n']
        return dumps(cur_state)+'\n'
