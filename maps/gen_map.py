import random
from collections import defaultdict

def generate_map(old_map):
  new_map={
  "virusrad": 15,
  "maxX": 14142,
  "maxY": 14142,
  "ffieldcircle": [],
  "food": [],
  "virus": [],
  "ffieldsquare": []
  }
  #generates a map of 10 food,5 viruses,2 force fields of square and circle each
  for i in range(10):
      new_map["food"].append([random.randrange(0,14142),random.randrange(0,14142)])
  for i in range(5):
      new_map["virus"].append([random.randrange(0,14142),random.randrange(0,14142)])
  for i in range(2):
      fsquare=defaultdict()
      fsquare["origin"]=[random.randrange(0,14142),random.randrange(0,14142)]
      fsquare["innerrad"]=random.randrange(1,75)
      fsquare["outerrad"]=random.randrange(1,75)
      new_map["ffieldsquare"].append(fsquare)
      fcircle=defaultdict()
      fcircle["origin"]=[random.randrange(0,14142),random.randrange(0,14142)]
      fcircle["innerrad"]=random.randrange(0,14142)
      fcircle["outerrad"]=random.randrange(0,14142)
      new_map["ffieldsquare"].append(fcircle)

  return new_map
