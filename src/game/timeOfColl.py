'''
Author: Brian Stone <modeofoperations@gmail.com>
Date: April 15, 2010

Modified by:
Vasantha Ganesh <vasanthaganesh.k@tuta.io>
Febrauary 2017

This code is licensed under GNU GPLV3

This program demonstrates how to calculate the time of impact or time of closest
approach of two circles moving with constant velocity.

'''

from math import sqrt, sin, cos, radians
import operator

def TimeOfClosestApproach(bota, botb):
    Pba = map(operator.sub, botb['center'], bota['center'])
    Ra = bota['radius']
    Rb = botb['radius']

    vela, velb = bota['velocity'], botb['velocity']
    anga, angb = bota['angle'], botb['angle']
    
    vx = velb*cos(radians(angb)) - vela*cos(radians(anga))
    vy = velb*sin(radians(angb)) - velb*sin(radians(anga))

    Vba = (vx, vy)
    
    a = sum(map(operator.mul, Vba, Vba))
    
    b = 2 * sum(map(operator.mul, Pba, Vba))

    c = sum(map(operator.mul, Pba, Pba)) - (Ra**2)

    discriminant = b * b - 4 * a * c;

    if discriminant < 0:
        t = -b / (2 * a);

    else:
        t0 = (-b + sqrt(discriminant)) / (2 * a)    
        t1 = (-b - sqrt(discriminant)) / (2 * a)
        
        t = min(t0, t1)
    return t
