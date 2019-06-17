# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs
import spin

import math

def Carom(ball, table, timeStep):
    
    rightRail = ball.Loc.x + ball.radius + table.cushionThickness >= table.length
    leftRail = ball.Loc.x - ball.radius - table.cushionThickness <= 0
    topRail = ball.Loc.y + ball.radius + table.cushionThickness >= table.width
    bottomRail = ball.Loc.y - ball.radius - table.cushionThickness <= 0
    noEnglish = ball.spinZ == 0
    posEnglish = ball.spinZ > 0
    negEnglish = ball.spinZ < 0
    posXvel = ball.Vel.x > 0
    negXvel = ball.Vel.x < 0
    posYvel = ball.Vel.y > 0
    negYvel = ball.Vel.y < 0
    
    #checking to see if the ball is near a pocket.
    for pocket in table.pocketList:
        if math.hypot(pocket.Loc.x - ball.Loc.x, pocket.Loc.y - ball.Loc.y) <= table.cornerPocketDepth:
            print("ball near pocket")
    
    #this kind of works, but it is not exactly right.  
    #I should be calculating the velocity of the outside of the ball added to the linear velocity of the ball
    if rightRail or leftRail:
        prevXvel = ball.Vel.x
        ball.Vel.x *= -1 * table.cushion_damper_coef
        ball.Loc.x = table.length - table.cushionThickness - ball.radius if rightRail else table.cushionThickness + ball.radius
        accX = prevXvel - ball.Vel.x / timeStep
        normalF = ball.mass * accX
        ffy = normalF * table.feltFrictionCo
        if ball.spinZ == 0 : return
        posSpin = True if ball.spinZ > 0 else False
        if (posSpin and rightRail) or (not posSpin and leftRail): ffy *= -1
        torque = ffy * ball.radius
        alpha = torque / ball.momentOfInertia
        ball.spinZ += alpha * timeStep
        accY = ffy / ball.mass
        ball.Vel.y += accY * timeStep
        
    elif topRail or bottomRail:
        prevYvel = ball.Vel.y
        ball.Vel.y *= -1 * table.cushion_damper_coef
        ball.Loc.y = table.width - table.cushionThickness - ball.radius if topRail else table.cushionThickness + ball.radius
        accY = prevYvel - ball.Vel.y / timeStep
        normalF = ball.mass * accY
        ffX = normalF * table.feltFrictionCo
        if ball.spinZ == 0 : return
        posSpin = True if ball.spinZ > 0 else False
        if posSpin and bottomRail or not posSpin and topRail: ffX *= -1
        torque = ffX * ball.radius
        alpha = torque / ball.momentOfInertia
        ball.spinZ += alpha * timeStep
        accX = ffX / ball.mass
        ball.Vel.x += accX * timeStep
    

if __name__ == "__main__":
    
    table = tableballdefs.Table()
    ball = tableballdefs.Ball(1,2,table.length,table.width/2,2,2,-2)
    
    Carom(ball, table, 0.01)
    
    print(ball.Vel.x, ball.Vel.y, ball.spinX, ball.spinY, ball.spinZ)