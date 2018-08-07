# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs

def Carom(ball, table, timeStep):
    
    if ball.Loc.x + ball.radius >= table.length :
        prevVel = ball.Vel.x
        ball.Vel.x = -1 * table.cushionBounce * ball.Vel.x
        ball.Loc.x = table.length - ball.radius
        
        if ball.english == 0 : return True
        elif ball.english < 0 :
            accX = (prevVel - ball.Vel.x)/(timeStep)
            normal = accX * ball.mass
            frictionForce = normal * table.feltFrictionCo
            ball.Vel.y += (accY * timeStep)
            torqueFriction = frictionForce * ball.radius
            alpha = torqueFriction / ball.momentOfInertia
            print(ball.english)
            ball.english -= (alpha * timeStep)
        elif ball.english > 0 :
        
        return True
    
    elif ball.Loc.x - ball.radius <= 0 :
        ball.Vel.x = -1 * table.cushionBounce * ball.Vel.x
        ball.Loc.x = ball.radius
        
        return True
    
    if ball.Loc.y + ball.radius >= table.width : 
        ball.Vel.y = -1 * table.cushionBounce * ball.Vel.y
        ball.Loc.y = table.width - ball.radius
        
        return True
    
    elif ball.Loc.y - ball.radius <= 0 :
        ball.Vel.y = -1 * table.cushionBounce * ball.Vel.y
        ball.Loc.y = ball.radius
        
        return True
    
    return False
    
def CalcAcc(v0, v1, timeStep):
    return (v0 - v1) / timeStep
    

if __name__ == "__main__":
    
    table = tableballdefs.Table()
    ball = tableballdefs.Ball(1,0,table.length,table.width/2,-2,0)
    
    Carom(ball, table, 0.01)
    
    print(ball.Vel.x, ball.Vel.y, ball.english)