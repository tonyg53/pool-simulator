# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:47:40 2018

@author: tony.gold
"""

import tableballdefs


def Test():
    ball = tableballdefs.Ball(1,1,0,0,0,-105,100)
    table = tableballdefs.Table()
    timeStep = 0.1
    frictionForceFWD = TopSpin(ball, table, timeStep)
    frictionForceSide = SideSpin(ball, table, timeStep)
    
    while frictionForceFWD != 0 or frictionForceSide != 0:
        frictionForceFWD = TopSpin(ball, table, timeStep)
        frictionForceSide = SideSpin(ball, table, timeStep)
        
        print("topSpin ",ball.topSpin * ball.radius, " sideSpin ",ball.sideSpin * ball.radius, " velocity ", ball.Vel.getLength(), " fwd FF ", frictionForceFWD, " side FF ", frictionForceSide)

def TopSpin(ball, table, timeStep):
    vel = ball.Vel.getLength()
    alpha = SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo)
    ff = SolveFF(ball.mass, table.feltFrictionCo)
    if DidBallGrip(vel, alpha, timeStep, ball.topSpin, ball.radius): 
        ball.topSpin = vel/ball.radius
        return 0
    if vel > ball.topSpin * ball.radius:
        ff *= -1
    if vel < ball.topSpin * ball.radius:
        alpha *= -1
    ball.topSpin += alpha * timeStep
    return ff

def SideSpin(ball, table, timeStep):
    if ball.sideSpin == 0 : 
        return 0
    alpha = SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo)

    ff = SolveFF(ball.mass, table.feltFrictionCo)
    if ball.sideSpin > 0 : 
        alpha *= -1
    if ball.sideSpin < 0 :
        ff *= -1
    if abs(alpha * timeStep) >= abs(ball.sideSpin):
        ball.sideSpin = 0
        return 0
    ball.sideSpin += alpha * timeStep
    return ff
    
def SolveAlpha(mass, radius, moi, frictionCo):
    ff = SolveFF(mass, frictionCo)
    torqueFF = ff * radius
    return torqueFF / moi  

def SolveFF(mass, frictionCo):
    return mass * 9.8 * frictionCo

def DidBallGrip(vel, alpha, timeStep, omega, radius):
    if abs(abs(omega) - abs(alpha * timeStep)) * radius <= vel :
        return True
    return False
    
if __name__ == "__main__":
    Test()