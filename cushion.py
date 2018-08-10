# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs

import math

def Carom(ball, table, timeStep):
    
    rightRail = ball.Loc.x + ball.radius >= table.length
    leftRail = ball.Loc.x - ball.radius <= 0
    topRail = ball.Loc.y + ball.radius >= table.width
    bottomRail = ball.Loc.y - ball.radius <= 0
    noEnglish = ball.english == 0
    posEnglish = ball.english > 0
    negEnglish = ball.english < 0
    posXvel = ball.Vel.x > 0
    negXvel = ball.Vel.x < 0
    posYvel = ball.Vel.y > 0
    negYvel = ball.Vel.y < 0
    
    #just a quick reminder that i need to impliment logic for pocketing balls.
    if (rightRail and (topRail or bottomRail)) or (leftRail and (topRail or bottomRail)):
        print('ball hit 2 rails at the same time, you need to impliment pockets now')
    
    if rightRail or leftRail:
        
        topSpinSign = 1 if ball.topSpin > 0 else -1
        topSpinFFangle = math.pi / 2 + math.atan2(ball.Vel.y, ball.Vel.x)
        topSpinFF = topSpinSign * ball.mass * 9.8 * table.feltFrictionCo
        
        ffY = topSpinFF * math.cos(topSpinFFangle)
        
        accY = ffY / ball.mass
        
        prevVel = ball.Vel.x
        ball.Vel.x = -1 * table.cushionBounce * ball.Vel.x
        
        ball.Loc.x = table.length - ball.radius if rightRail else ball.radius
                
        if noEnglish and ball.Vel.x == 0: return True
        
        frictionForce = CalcFF(prevVel, ball.Vel.x, timeStep, ball.mass, table.feltFrictionCo)
        accY += CalcAccPara(frictionForce, ball.mass)
        alpha = CalcAlpha(frictionForce, ball.radius, ball.momentOfInertia)
                        
        if ((noEnglish and negYvel) or negEnglish) and rightRail:
            ball.Vel.y += (accY * timeStep)
            ball.english += (alpha * timeStep)
            
        elif ((noEnglish and posYvel) or posEnglish) and rightRail:
            ball.Vel.y -= (accY * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif ((noEnglish and negYvel) or negEnglish) and leftRail:
            ball.Vel.y += (accY * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif ((noEnglish and posYvel) or posEnglish) and leftRail:
            ball.Vel.y -= (accY * timeStep)
            ball.english += (alpha * timeStep)
        
        
        return True
    
    if topRail or bottomRail : 
              
        topSpinSign = 1 if ball.topSpin > 0 else -1 
        topSpinFFangle = math.atan2(ball.Vel.y, ball.Vel.x)
        topSpinFF = topSpinSign * ball.mass * 9.8 * table.feltFrictionCo
        
        ffX = topSpinFF * math.cos(topSpinFFangle)
        
        accX = ffX / ball.mass
        
        prevVel = ball.Vel.y
        ball.Vel.y = -1 * table.cushionBounce * ball.Vel.y
        
        ball.Loc.y = table.width - ball.radius if topRail else ball.radius
        
        if noEnglish and ball.Vel.x == 0: return True
        
        frictionForce = CalcFF(prevVel, ball.Vel.y, timeStep, ball.mass, table.feltFrictionCo)
        accX += CalcAccPara(frictionForce, ball.mass)
        alpha = CalcAlpha(frictionForce, ball.radius, ball.momentOfInertia)
        
        if ((noEnglish and posXvel) or negEnglish) and topRail:
            ball.Vel.x -= (accX * timeStep)
            ball.english += (alpha * timeStep)
            
        elif ((noEnglish and negXvel) or posEnglish) and topRail:
            ball.Vel.x += (accX * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif ((noEnglish and posXvel) or negEnglish) and bottomRail:
            ball.Vel.x -= (accX * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif ((noEnglish and negXvel) or posEnglish) and bottomRail:
            ball.Vel.x += (accX * timeStep)
            ball.english += (alpha * timeStep)
            
        return True
    
    return False
    
def CalcFF(v0, v1, timeStep, mass, coef):
    acc = (v0 - v1) / timeStep
    norm = acc * mass
    return norm * coef

def CalcAccPara(ff, mass):
    return ff / mass

def CalcAlpha(ff, radius, moi):
    torq = ff * radius
    return torq / moi
    

if __name__ == "__main__":
    
    table = tableballdefs.Table()
    ball = tableballdefs.Ball(1,+2,table.length,table.width/2,0,2)
    
    Carom(ball, table, 0.01)
    
    print(ball.Vel.x, ball.Vel.y, ball.english)