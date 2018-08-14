# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:30:21 2018

@author: tony.gold
"""

import tableballdefs
import math

def aim(cueBall, objBall):
    azmuth = math.atan2(objBall.Loc.y - cueBall.Loc.y, objBall.Loc.x - cueBall.Loc.x)
    
    return azmuth

if __name__ == "__main__":
    ball1 = tableballdefs.Ball()
    ball2 = tableballdefs.Ball()
    aim(ball1, ball2)