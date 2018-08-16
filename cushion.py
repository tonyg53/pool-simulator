# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs
import spin

import math

def Carom(ball, table, timeStep):
    
    rightRail = ball.Loc.x + ball.radius >= table.length
    leftRail = ball.Loc.x - ball.radius <= 0
    topRail = ball.Loc.y + ball.radius >= table.width
    bottomRail = ball.Loc.y - ball.radius <= 0
    noEnglish = ball.spinZ == 0
    posEnglish = ball.spinZ > 0
    negEnglish = ball.spinZ < 0
    posXvel = ball.Vel.x > 0
    negXvel = ball.Vel.x < 0
    posYvel = ball.Vel.y > 0
    negYvel = ball.Vel.y < 0
    
    #just a quick reminder that i need to impliment logic for pocketing balls.
    if (rightRail and (topRail or bottomRail)) or (leftRail and (topRail or bottomRail)):
        print('ball hit 2 rails at the same time, you need to impliment pockets now')
    
    if rightRail:
        prevXvel = ball.Vel.x
        ball.Vel.x *= -1 * table.cushionBounce
        ball.Loc.x = table.length - ball.radius
        accX = prevXvel - ball.Vel.x / timeStep
        normalF = ball.mass * accX
        ffy = normalF * table.feltFrictionCo
        if ball.spinZ == 0 : return
        posSpin = True if ball.spinZ > 0 else False
        if posSpin : ffy *= -1
        torque = ffy * ball.radius
        alpha = torque / ball.momentOfInertia
        ball.spinZ += alpha * timeStep
        accY = ffy / ball.mass
        ball.Vel.y += accY * timeStep
        
    

if __name__ == "__main__":
    
    table = tableballdefs.Table()
    ball = tableballdefs.Ball(1,+2,table.length,table.width/2,0,2)
    
    Carom(ball, table, 0.01)
    
    print(ball.Vel.x, ball.Vel.y, ball.english)