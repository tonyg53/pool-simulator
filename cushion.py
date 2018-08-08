# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs

def Carom(ball, table, timeStep):
    
    rightRail = ball.Loc.x + ball.radius >= table.length
    leftRail = ball.Loc.x - ball.radius <= 0
    topRail = ball.Loc.y + ball.radius >= table.width
    bottomRail = ball.Loc.y - ball.radius <= 0
    noEnglish = ball.english == 0
    posEnglish = ball.english > 0
    negEnglish = ball.english < 0
    
    if rightRail or leftRail:
        prevVel = ball.Vel.x
        ball.Vel.x = -1 * table.cushionBounce * ball.Vel.x
        
        if rightRail : ball.Loc.x = table.length - ball.radius
        else : ball.Loc.x = ball.radius
        
        if noEnglish and ball.Vel.x == 0: return True
        
        frictionForce = CalcFF(prevVel, ball.Vel.x, timeStep, ball.mass, table.feltFrictionCo)
        accY = CalcAccPara(frictionForce, ball.mass)
        alpha = CalcAlpha(frictionForce, ball.radius, ball.momentOfInertia)
        
        if negEnglish and rightRail:
            ball.Vel.y += (accY * timeStep)
            ball.english += (alpha * timeStep)
            
        elif posEnglish and rightRail:
            ball.Vel.y -= (accY * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif negEnglish and leftRail:
            ball.Vel.y += (accY * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif posEnglish and leftRail:
            ball.Vel.y -= (accY * timeStep)
            ball.english += (alpha * timeStep)
        
        return True
    
    if topRail or bottomRail : 
        prevVel = ball.Vel.y
        ball.Vel.y = -1 * table.cushionBounce * ball.Vel.y
        
        if topRail : ball.Loc.y = table.width - ball.radius
        else : ball.Loc.y = ball.radius
        
        if noEnglish and ball.Vel.x == 0: return True
        
        frictionForce = CalcFF(prevVel, ball.Vel.y, timeStep, ball.mass, table.feltFrictionCo)
        accX = CalcAccPara(frictionForce, ball.mass)
        alpha = CalcAlpha(frictionForce, ball.radius, ball.momentOfInertia)
        
        if negEnglish and topRail:
            ball.Vel.x -= (accX * timeStep)
            ball.english += (alpha * timeStep)
            
        elif posEnglish and topRail:
            ball.Vel.x += (accX * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif negEnglish and bottomRail:
            ball.Vel.x -= (accX * timeStep)
            ball.english -= (alpha * timeStep)
            
        elif posEnglish and bottomRail:
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
    ball = tableballdefs.Ball(0,-1,table.length/2,0,2,0)
    
    Carom(ball, table, 0.01)
    
    print(ball.Vel.x, ball.Vel.y, ball.english)