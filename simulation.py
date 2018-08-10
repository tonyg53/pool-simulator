# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:53:17 2018

@author: tony.gold
"""
import tableballdefs
import collision
import plotballs
import topspin
import cushion

import math
import itertools

class Simulation(object):
    
    def __init__(self, numballs, ballList, shot, table = tableballdefs.Table()):
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
                    ball.zeroVel()
                    countStoppedBalls = countStoppedBalls + 1
                    
                        
                else:
                    ballsMoving = True
                    #check to see if the ball has hit a wall, if so solve the new velocity
                    cushion.Carom(ball, self.table, timeStep)
                    
                    #update the ball velocity from the acceleration
                    ball.Loc.x = ball.Loc.x + (ball.Vel.x * timeStep)
                    ball.Loc.y = ball.Loc.y + (ball.Vel.y * timeStep)
                    self.plot.plotPoint(k, ball.Loc.x, ball.Loc.y)
                    
                    frictionForce = topspin.Solve(ball, self.table, timeStep)
                    
                    #calculate the acceleration based on the table and ball conditions
                    acc = -(2*9.8*self.table.feltThickness)/(3*ball.radius*ball.radius) + (frictionForce/ball.mass)
                    
                    alpha = math.atan2(ball.Vel.y,ball.Vel.x)
                    
                    xAcc = math.cos(alpha) * acc
                    yAcc = math.sin(alpha) * acc
                    
                    ball.Vel.x = ball.Vel.x + (xAcc * timeStep)
                    ball.Vel.y = ball.Vel.y + (yAcc * timeStep)
                     
            for ball1, ball2 in itertools.combinations(self.ballList, 2):
                 if collision.happened(ball1, ball2) : collision.run(ball1, ball2)
                
            if countStoppedBalls == self.numballs : ballsMoving = False
            elapsedTime = elapsedTime + timeStep
            
        return self.ballList
            
