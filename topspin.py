# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:47:40 2018

@author: tony.gold
"""

import tableballdefs
import plotballs

def Test():
    ball = tableballdefs.Ball(1,1,0,0,0,105)
    table = tableballdefs.Table()
    plot = plotballs.PlotBalls(1, table)
    timeStep = 0.1
    frictionForce = Solve(ball, table, timeStep)
    
    while frictionForce != 0:
        print("topSpin ",ball.topSpin * ball.radius, " velocity ", ball.Vel.getLength(), " friction force ", frictionForce)
        frictionForce = Solve(ball, table, timeStep)

def Solve(ball, table, timeStep):
    #eventually this grabFactor will should be changed to static coefficient of friction
    grabFactor = 0.03
    vel = ball.Vel.getLength()
    if vel >= (ball.topSpin * ball.radius) - grabFactor and vel <= (ball.topSpin * ball.radius) + grabFactor: 
        ball.topSpin = vel/ball.radius
        return 0
    elif ball.Vel.getLength() > ball.topSpin * ball.radius:
        frictionForce = ball.mass * 9.8 * table.feltFrictionCo
        torqueFriction = frictionForce * ball.radius
        alpha = torqueFriction / ball.momentOfInertia
        ball.topSpin = ball.topSpin + (alpha * timeStep)
        return -1 * frictionForce
    elif ball.Vel.getLength() < ball.topSpin * ball.radius:
        frictionForce = ball.mass * 9.8 * table.feltFrictionCo
        torqueFriction = frictionForce * ball.radius
        alpha = torqueFriction / ball.momentOfInertia
        ball.topSpin = ball.topSpin - (alpha * timeStep)
        return frictionForce

    
if __name__ == "__main__":
    Test()