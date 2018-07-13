# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:21:17 2018

@author: tony.gold
"""

import tableballdefs
import math

def happened(ball1, ball2):
    dist = math.hypot(ball1.Loc.x - ball2.Loc.x, ball1.Loc.y - ball2.Loc.y)
    collisionDist = (ball1.diameter / 2) + (ball2.diameter / 2)
    
    if dist <= collisionDist: return True
    else: return False

def run(ball1, ball2):
    
    collisionAngle = math.atan2((ball2.Loc.y - ball1.Loc.y), (ball2.Loc.x - ball1.Loc.x))
    
    speed1 = ball1.Vel.length
    speed2 = ball2.Vel.length
   
    dir1 = math.atan2(ball1.Vel.y, ball1.Vel.x)
    dir2 = math.atan2(ball2.Vel.y, ball2.Vel.y)
    
    newXSpeed1 = speed1 * math.cos(dir1 - collisionAngle)
    newYSpeed1 = speed1 * math.sin(dir1 - collisionAngle)
    newXSpeed2 = speed2 * math.cos(dir2 - collisionAngle)
    newYSpeed2 = speed2 * math.sin(dir2 - collisionAngle)
    
    finalXSpeed1 = ((ball1.mass - ball2.mass) * newXSpeed1 + (ball2.mass + ball2.mass) * newXSpeed2) / (ball1.mass + ball2.mass)
    finalXSpeed2 = ((ball1.mass + ball2.mass) * newXSpeed1 + (ball2.mass - ball1.mass) * newXSpeed2) / (ball1.mass + ball1.mass)
    
    finalYSpeed1 = newYSpeed1
    finalYSpeed2 = newYSpeed2
    
    cosAngle = math.cos(collisionAngle)
    sinAngle = math.sin(collisionAngle)
   
    ball1.Vel.x = cosAngle * finalXSpeed1 - sinAngle * finalYSpeed1
    ball1.Vel.y = sinAngle * finalXSpeed1 + cosAngle * finalYSpeed1
    ball2.Vel.x = cosAngle * finalXSpeed2 - sinAngle * finalYSpeed2
    ball2.Vel.y = sinAngle * finalXSpeed2 + cosAngle * finalYSpeed2
    
    print("collision ball1 vel:", math.hypot(ball1.Vel.x, ball1.Vel.y), "collision ball2 vel:", math.hypot(ball2.Vel.x, ball2.Vel.y))
        
if __name__ == "__main__":
    run(tableballdefs.Ball(1.55,0,0.0572,0.165,0.99,0.68,0.68,0,0), tableballdefs.Ball(0,0,0.572,0.165,0.99,2.057,0.68,0,0))