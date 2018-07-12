# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:21:17 2018

@author: tony.gold
"""

import tableballdefs
import math

def run(ball1, ball2):
    dist = math.hypot(ball1.xLoc - ball2.xLoc, ball1.yLoc - ball2.yLoc)
    collisionDist = (ball1.diameter / 2) + (ball2.diameter / 2)
    
    #we have a collision
    if dist <= collisionDist:
        print("Collision")
    
    
if __name__ == "__main__":
    run(tableballdefs.Ball(), tableballdefs.Ball())