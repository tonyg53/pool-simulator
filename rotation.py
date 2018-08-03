# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:47:40 2018

@author: tony.gold
"""

import tableballdefs

def Test():
    ball = tableballdefs.Ball(1,1)
    table = tableballdefs.Table()
    timeStep = 0.1
    ideal = True
    while ideal:
        ideal = Solve(ball, table, timeStep)
        print("topSpin ",ball.topSpin * ball.radius, " velocity ", ball.Vel.getLength())

def Solve(ball, table, timeStep):
    if ball.Vel.getLength() == ball.topSpin * ball.radius: return False
    elif ball.Vel.getLength() > ball.topSpin * ball.radius:
        frictionForce = ball.mass * 9.8 * table.feltFrictionCo
        torqueFriction = frictionForce * ball.radius
        alpha = torqueFriction / ball.momentOfInertia
        ball.topSpin = ball.topSpin + (alpha * timeStep)
        return True
    elif ball.Vel.getLength() < ball.topSpin * ball.radius:
        frictionForce = ball.mass * 9.8 * table.feltFrictionCo
        torqueFriction = frictionForce * ball.radius
        alpha = torqueFriction / ball.momentOfInertia
        ball.topSpin = ball.topSpin - (alpha * timeStep)
        return True
        
        
    
if __name__ == "__main__":
    Test()