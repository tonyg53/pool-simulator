# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:35:15 2018

@author: tony.gold
"""
import math

class Table(object):
    
    def __init__(self, length = 9, feltFrictionCo = 0.1, cushionBounce = 0.65):
        self.length = length * 0.3048
        self.width = (length / 2) * 0.3048
        self.feltFrictionCo = feltFrictionCo
        self.cushionBounce = cushionBounce

class Ball(object):
    
    def __init__(self, xVel = 0, yVel=0, diameter = 57.2, mass = 165, elasticity = 0.99, xLoc = 0, yLoc = 0, english = 0, topSpin = 0):
        self.diameter = diameter
        self.mass = mass
        self.elasticity = elasticity
        self.xVel = xVel
        self.yVel = yVel
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.english = english
        self.topSpin = topSpin
        
class Shot(object):
    
    def __init__(self, cueBall = Ball(), shotAzmuth = 0, cueStickMass = 20, cueStickVelocity = 2, cueStickCOR = 0.85, strikePtDistFromCenter = 0, strikePtAngle = 0):
        self.cueStickMass = cueStickMass * 0.0283495
        self.cueStickVelocity = cueStickVelocity
        self.cueStickCOR = cueStickCOR
        self.strikePtDistFromCenter = strikePtDistFromCenter
        self.strikePtAngle = strikePtAngle
        self.shotAzmuth = shotAzmuth
        self.cueBall = cueBall
        
    def execute(self):
        if self.cueBall.xVel != 0 and self.cueBall.yVel !=0 : raise "wait for balls to stop"

        stickForce = self.cueStickMass * self.cueStickVelocity
        ballVel = stickForce/(self.cueBall.mass + self.cueStickMass)
        self.cueBall.xVel = math.cos(math.radians(self.shotAzmuth))*ballVel
        self.cueBall.yVel = math.sin(math.radians(self.shotAzmuth))*ballVel
        return self.cueBall

def zeroVels(ball):
    ball.xVel = 0
    ball.yVel = 0
    return ball
      
    
def main():
    table = Table()
    ballList = []
    numBalls = 2
    
    for i in range(0,numBalls):
        ballList.append( Ball() )
        
    ballList[0].xLoc = table.length / 4
    ballList[0].yLoc = table.width / 2
    ballList[1].xLoc = table.length * 3/4
    ballList[1].xLoc = table.width / 2
    
    brake = Shot(ballList[0])
    brake.execute()
    ballsMoving = True
    timeStep = 0.01
    
    while ballsMoving :
        for ball in ballList:
            countStoppedBalls = 0
            if ball.xVel != 0 and ball.yVel != 0: 
                ballsMoving = True
                
                #check to see if the ball has hit a wall, if so reverse the velocity dir
                if ball.xLoc >= table.length or ball.xLoc <= 0 : 
                    ball.xVel = -1 * table.cushionBounce * ball.xVel
                if ball.yLoc >= table.width or ball.yLoc <= 0 : 
                    ball.yVel = -1 * table.cushionBounce * ball.yVel
                
                #update the ball velocity from the acceleration
                ball.xLoc = ball.xLoc + (ball.xVel * timeStep)
                ball.yLoc = ball.yLoc + (ball.yVel * timeStep)
                radius = ball.diameter / 2
                
                #calculate the acceleration based on the table and ball conditions
                acc = -(2*9.8*0.001)/(3*radius*radius)
                if ball.xVel >= 0 : xPositive = True
                else: xPositive = False
                alpha = math.atan(ball.yVel/ball.xVel)
                
                #this code accounts for ball moving in negitave directions
                if xPositive:
                    xAcc = math.cos(alpha) * acc
                else:
                    xAcc = -1 * math.cos(alpha) * acc
                yAcc = math.sin(alpha) * acc
                
                ball.xVel = ball.xVel + (xAcc * timeStep)
                ball.yVel = ball.yVel + (yAcc * timeStep)
                
                print("x pos: ",ball.xLoc," y pos: ",ball.yLoc)
                
            else: 
                countStoppedBalls = countStoppedBalls + 1
                
            if countStoppedBalls == numBalls : ballsMoving = False
            
            
            

if __name__ == "__main__":
    main()