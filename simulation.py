# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:53:17 2018

@author: tony.gold
"""
import tableballdefs
import collision
import plotballs
import spin
import cushion2

import math
import itertools

class Simulation(object):
    
    def __init__(self, numballs, ballList, shot, table):
        self.table = table
        self.ballList = ballList
        self.numballs = numballs
        self.shot = shot
        self.plot = plotballs.PlotBalls(self.numballs, self.table)
        
    def run(self):
            
        for i, ball in enumerate(self.ballList):
            self.plot.plotPoint(i, ball.Loc.x, ball.Loc.y)
            
        self.shot.execute()
        ballsMoving = True
        timeStep = 0.01
        stopVel = 0.05
        elapsedTime = 0
        
        while ballsMoving :
            countStoppedBalls = 0
            for k, ball in enumerate(self.ballList): 
                
                if ball.Vel.getLength() <= stopVel:
#                    alpha = spin.SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, self.table.feltFrictionCo)
#                    if spin.DidBallGrip(ball.Vel.x, alpha, timeStep, ball.spinY, ball.radius):
#                        print('ball griped')
#                    else: print('ball slipped')
                        
                    ball.zeroVel()
                    countStoppedBalls = countStoppedBalls + 1
                    
                else:
                    ballsMoving = True
                    
                    #update the ball location
                    ball.Loc.x += (ball.Vel.x * timeStep)
                    ball.Loc.y += (ball.Vel.y * timeStep)
                    self.plot.plotPoint(k, ball.Loc.x, ball.Loc.y)
                    
                    #check to see if the ball has hit a wall, if so solve the new velocity
                    cushion2.Carom(ball, self.table, timeStep)
                    
                    #apply friction
                    frictionForceY = spin.SpinX(ball, self.table, timeStep)
                    frictionForceX = spin.SpinY(ball, self.table, timeStep)
                    
                    #calculate the acceleration based on the table and ball conditions
                    acc = -(2*9.8*self.table.feltThickness)/(3*ball.radius*ball.radius)
                    
                    alpha = math.atan2(ball.Vel.y,ball.Vel.x)
                    
                    xAcc = math.cos(alpha) * acc + frictionForceX/ball.mass
                    yAcc = math.sin(alpha) * acc + frictionForceY/ball.mass
                    
                    ball.Vel.x = ball.Vel.x + (xAcc * timeStep)
                    ball.Vel.y = ball.Vel.y + (yAcc * timeStep)
                     
            for ball1, ball2 in itertools.combinations(self.ballList, 2):
                 if collision.happened(ball1, ball2) : 
                     collision.run(ball1, ball2)
                
            if countStoppedBalls == self.numballs : ballsMoving = False
            elapsedTime += timeStep
        
        self.plot.showPlot()
        return self.ballList
            
