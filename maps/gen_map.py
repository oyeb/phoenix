from random import randrange
from collections import defaultdict

def generate_map(old_map):
  new_map={
  "virusrad": 35,
  "maxX": 14142,
  "maxY": 14142,
  "ffieldcircle": [],
  "food": [],
  "virus": [],
  "ffieldsquare": []
  }
  no_of_food = randrange(50,80)
  for i in xrange(no_of_food):
      new_map["food"].append([randrange(0,14142),randrange(0,14142)])
  no_of_virus = randrange(50,80)
  for i in xrange(no_of_virus):
      new_map["virus"].append([randrange(0,14142),randrange(0,14142)])
  no_of_ffields = randrange(20,40)
  for i in xrange(no_of_ffields):
      fsquare=defaultdict()
      fsquare["origin"]=[randrange(0,14050),randrange(0,14050)]
      fsquare["innerside"]=randrange(1,50)
      fsquare["outerside"]=randrange(51,80)
      new_map["ffieldsquare"].append(fsquare)
      fcircle=defaultdict()
      fcircle["origin"]=[randrange(0,14050),randrange(0,14050)]
      fcircle["innerrad"]=randrange(1,50)
      fcircle["outerrad"]=randrange(51,75)
      new_map["ffieldsquare"].append(fcircle)

  return new_map
