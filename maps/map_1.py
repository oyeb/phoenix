from random import randrange
from collections import defaultdict

def generate_map(old_map):
  new_map={
  "virusrad": 10,
  "maxX": 4992,
  "maxY": 2808,
  "ffieldcircle": [],
  "food": [],
  "virus": [],
  "ffieldsquare": []
  }
  no_of_food = randrange(800,1000)
  for i in xrange(no_of_food):
      new_map["food"].append([randrange(0,4992),randrange(0,2808)])
  new_map["virus"].append(280,2800)
  new_map["virus"].append(2800,1400)
  new_map["virus"].append(1400,700)
  new_map["virus"].append(10,1000)
  new_map["virus"].append(3000,2000)
  new_map["virus"].append(2800,700)
  new_map["virus"].append(2500,20)
  new_map["virus"].append(1600,1500)
  new_map["virus"].append(2900,2200)
  new_map["virus"].append(500,200)
  new_map["virus"].append(4000,1700)
  new_map["virus"].append(3500,2700)
  fsquare=defaultdict()
  fsquare["origin"]=[1900,1000]
  fsquare["innerside"]=randrange(1,30)
  fsquare["outerside"]=randrange(31,60)
  new_map["ffieldsquare"].append(fsquare)
  fcircle=defaultdict()
  fcircle["origin"]=[2300,2400]
  fcircle["innerrad"]=randrange(1,20)
  fcircle["outerrad"]=randrange(21,50)
  fcircle_1=defaultdict()
  fcircle["origin"]=[4000,1000]
  fcircle["innerrad"]=randrange(1,20)
  fcircle["outerrad"]=randrange(21,50)
  new_map["ffieldsquare"].append(fcircle_1)

  return new_map
