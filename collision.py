# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:21:17 2018

@author: tony.gold
"""

import tableballdefs
import math

def happened(ball1, ball2):
    dist = math.hypot(ball1.Loc.x - ball2.Loc.x, ball1.Loc.y - ball2.Loc.y)
    collisionDist = (ball1.radius) + (ball2.radius)
    
    if dist <= collisionDist: return True
    else: return False

def run(ball1, ball2):
    
    collisionAngle = math.atan2((ball2.Loc.y - ball1.Loc.y), (ball2.Loc.x - ball1.Loc.x))
    dist = math.hypot(ball2.Loc.x - ball1.Loc.x, ball2.Loc.y - ball1.Loc.y)
    
    if dist < (ball1.radius) + (ball2.radius):
        moveDist = ((ball1.radius) /2)#+ (ball2.radius)) / 2
        B1x = ball1.Loc.x - moveDist * math.cos(collisionAngle)
        B1y = ball1.Loc.y - moveDist * math.sin(collisionAngle)
        B2x = ball2.Loc.x + moveDist * math.cos(collisionAngle)
        B2y = ball2.Loc.y + moveDist * math.sin(collisionAngle)
        
        ball1.Loc.x = B1x
        ball1.Loc.y = B1y
        ball2.Loc.x = B2x
        ball2.Loc.y = B2y
    
    speed1 = ball1.Vel.getLength()
    speed2 = ball2.Vel.getLength()
   
    dir1 = math.atan2(ball1.Vel.y, ball1.Vel.x)
    dir2 = math.atan2(ball2.Vel.y, ball2.Vel.x)
    
    
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
        
if __name__ == "__main__":
    ball1 = tableballdefs.Ball(0,    0,0.68,  0.68,0,0)
    ball2 = tableballdefs.Ball(-1.50,0,0.7372,0.68,0,0)
    if happened(ball1, ball2):
        run(ball1, ball2)
    else: print("no collision")