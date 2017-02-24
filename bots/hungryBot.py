from botapi import game
import sys
import random,math
from __future__ import division
print "I'm Poppy!"
sys.stdout.flush()

while True:
    gs_json=raw_input()
    game_state=game(gs_json,"tinku")
    food = game_state.get_foods()
    for bot in game_state.get_children():
        mindist = 1000000
        
        for x in range(len(food)):
            dist=(food[x][0]-bot["center"][0])**2 + (food[x][1]-bot["center"][1])**2)
            if(dist<mindist):
                mindist=dist
                mincoord = food[x]
        
        angle = math.degrees(math.atan((bot["center"][1]-mincoord[1])/(bot["center"][0]-mincoord[0])))

        game_state.change_direction(bot["childno"],angle)

                
    print  game_state.make_move()
    sys.stdout.flush()
    
