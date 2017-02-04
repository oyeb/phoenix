from json import loads, dumps

class game:
    def __init__(self, json_text, name):
        self.game_state = loads(json_text)
        self.name = name
        self.move_obj = {}
        for bot in self.game_state['bots']:
            if bot['botname'] == self.name:
                self.move_obj[bot['childno']] = {
                    'childno': bot['childno'],
                    'relativeangle':0,
                    'ejectmass':0,
                    'split':False,
                    'pause':False}
        
    def change_direction(self, child_no, relative_angle):
        '''
        set new relative direction
        '''
        self.move_obj[child_no]['relativeangle'] = relative_angle

    def eject_mass(self, child_no):
        '''
        set if eject mass is true or not
        '''
        self.move_obj[child_no]['ejectmass'] = True

    def split(self, child_no):
        '''
        set if split in current direction is true or not. If the mass is not
        enough to split, then this command is ignored.
        '''
        self.move_obj[child_no]['split'] = True
        
    def pause(self, child_no):
        '''
        set if the bot has to be brought to a stand still
        '''
        self.move_obj[child_no]['pause'] = True

    def make_move(self):
        '''
        returns a move object in json format for all the children together
        '''
        return dumps(self.move_obj.values(), indent=4, sort_keys=True)

    def get_children(self):
        '''
        returns the list dicts with the details of children
        '''
        return filter(lambda x: x['botname'] == self.name, self.game_state['bots'])
    
    def get_bots(self):
        '''
        return a list of dicts with bot details:
        botname,
        childno,
        Xcoordinate,
        mass,
        angle,
        score
        '''
        return filter(lambda x: x['botname'] != self.name, self.game_state['bots'])

    def get_foods(self):
        '''
        return a list of tuples as x and y coordinates
        '''
        return list(map(lambda x: tuple(x), self.game_state['food']))

    def get_viruses(self):
        '''
        return a list of tuples as x and y coordinates
        '''
        return list(map(lambda x: tuple(x), self.game_state['virus']))

    def get_ffields_circle(self):
        '''
        return a list of dicts representing force-field / water-stream circles:
        innerrad,
        outerrad,
        origin
        '''
        return self.game_state['ffieldcircle']

    def get_ffields_square(self):
        '''
        return a list of dicts representing force-field / water-stream squares:
        origin,
        innerside,
        outerside
        '''
        return self.game_state['ffieldsquare']
