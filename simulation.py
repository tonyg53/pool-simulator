# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:53:17 2018

@author: tony.gold
"""
import tableballdefs
import collide
import math
import itertools

def main():
    table = tableballdefs.Table()
    ballList = []
    numBalls = 2
    
    for i in range(0,numBalls):
        ballList.append( tableballdefs.Ball() )
        
    ballList[0].xLoc = table.length / 4
    ballList[0].yLoc = table.width / 2
    ballList[1].xLoc = table.length * 3 / 4
    ballList[1].yLoc = table.width / 2
    
    brake = tableballdefs.Shot(ballList[0])
    brake.execute()
    ballsMoving = True
    timeStep = 0.01
    elapsedTime = 0
    
    while ballsMoving :
        countStoppedBalls = 0
        for ball in ballList: 
            if ball.xVel <= 0.005 and ball.xVel >= -0.005 and ball.yVel <= 0.005 and ball.yVel >= -0.005: 
                ball.xVel = 0
                ball.yVel = 0
                countStoppedBalls = countStoppedBalls + 1
                    
            else:
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
                acc = -(2*9.8*table.feltThickness)/(3*radius*radius)
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
                
                print("time :", elapsedTime, "x loc", ball.xLoc, "y loc: ",ball.yLoc, " x vel: ",ball.xVel," x acc: ",xAcc)
                #input()
        for ball1, ball2 in itertools.combinations(ballList, 2):
             collide.run(ball1, ball2)
                
        if countStoppedBalls == numBalls : ballsMoving = False
        elapsedTime = elapsedTime + timeStep
            
    return      
            

if __name__ == "__main__":
    main()