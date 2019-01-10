# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:47:40 2018

@author: tony.gold
"""

import tableballdefs


def Test():
    ball = tableballdefs.Ball(2.75,0,0,0,0,100,100)
    table = tableballdefs.Table()
    timeStep = 0.1
    frictionForceX = SpinX(ball, table, timeStep)
    frictionForceY = SpinY(ball, table, timeStep)
    
    while frictionForceX != 0 or frictionForceY != 0:
        frictionForceX = SpinX(ball, table, timeStep)
        frictionForceY = SpinY(ball, table, timeStep)
        print(ball.Vel.x, ball.Vel.y, frictionForceX, frictionForceY)

#returns the friction force due to the ball sliding, returns 0 if the ball is spinning at the same velocity as it's moving        
def SpinX(ball, table, timeStep):
    normal = 9.8 * ball.mass
    alpha = SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo, normal)
    ff = SolveFF(ball.mass, table.feltFrictionCo, normal)
    
    if DidBallGrip(ball.Vel.y, alpha, timeStep, ball.spinX, ball.radius):
        ball.spinX = -1 * ball.Vel.y / ball.radius
        return 0 
    if ball.Vel.y > ball.spinX * ball.radius: ff *= -1
    if ball.Vel.y < ball.spinX * ball.radius: alpha *= -1
    ball.spinX += alpha * timeStep
    return ff

#returns the friction force due to the ball sliding, returns 0 if the ball is spinning at the same velocity as it's moving
def SpinY(ball, table, timeStep):
    normal = 9.8 * ball.mass
    alpha = SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo, normal)
    ff = SolveFF(ball.mass, table.feltFrictionCo, normal)
    
    if DidBallGrip(ball.Vel.x, alpha, timeStep, ball.spinY, ball.radius):
        ball.spinY = ball.Vel.x / ball.radius
        return 0
    if ball.Vel.x > ball.spinY * ball.radius: ff *= -1
    if ball.Vel.x < ball.spinY * ball.radius: alpha *= -1
    ball.spinY += alpha * timeStep
    return ff
    
def SolveAlpha(mass, radius, moi, frictionCo, normal):
    ff = SolveFF(mass, frictionCo, normal)
    torqueFF = ff * radius
    return torqueFF / moi  

def SolveFF(mass, frictionCo, normalForce):
    return mass * normalForce * frictionCo

def DidBallGrip(vel, alpha, timeStep, omega, radius):
    if abs(abs(omega) - abs(alpha * timeStep)) * radius <= abs(vel) :
        return True
    return False
    
if __name__ == "__main__":
    Test()