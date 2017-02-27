from json import loads, dumps
import sys

class game:
    def __init__(self, name):
        self.game_state = loads(raw_input())
        self.name = name
        self.move_obj = {}
        for bot in self.game_state['bots']:
            if bot['botname'] == self.name:
                self.move_obj[bot['childno']] = {
                    'childno': bot['childno'],
                    'relativeangle':0,
                    'ejectmass':False,
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

    def send_move(self):
        '''
        returns a move object in json format for all the children together
        '''
        print dumps(self.move_obj.values())
        sys.stdout.flush()

    @staticmethod
    def send_acknowledgement():
        '''
        prints `I'm Poppy!` to STDOUT so that the engine can acknowledge the bot
        '''
        print "I'm Poppy!"
        sys.stdout.flush()

    def get_children(self):
        '''
        returns the list dicts with the details of children
        {
        'botname':'kevin',
        'childno':0,
        'center':[x, y],
        'mass':20,
        'angle':0,
        'radius':10
        }
        '''
        return filter(lambda x: x['botname'] == self.name, self.game_state['bots'])
    
    def get_blobs(self):
        '''
        returns a list of dicts of all the blobs other than your bot
        {
        'botname':'kevin',
        'childno':0,
        'center':[x, y],
        'mass':20,
        'angle':0,
        'radius':10
        }

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
