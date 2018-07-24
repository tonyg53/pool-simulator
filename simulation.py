# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:53:17 2018

@author: tony.gold
"""
import tableballdefs
import collision
import plotballs
import math
import itertools



def main():
    table = tableballdefs.Table()
    ballList = []
    numBalls = 4
    plot = plotballs.PlotBalls(numBalls, table)
    
    for i in range(0,numBalls):
        ballList.append( tableballdefs.Ball() )
        
    ballList[0].Loc.x = table.length / 5
    ballList[0].Loc.y = table.width / 3
    ballList[1].Loc.x = table.length * 3 / 4
    ballList[1].Loc.y = table.width / 2 + 0.01
    ballList[2].Loc.x = ballList[1].Loc.x + 0.01 + math.cos(math.radians(60))*ballList[1].diameter/2
    ballList[2].Loc.y = ballList[1].Loc.y + math.sin(math.radians(60))*ballList[1].diameter/2
    ballList[3].Loc.x = ballList[1].Loc.x + math.cos(math.radians(60))*ballList[1].diameter/2
    ballList[3].Loc.y = ballList[1].Loc.y - 0.01 - math.sin(math.radians(60))*ballList[1].diameter/2
    
    for i, ball in enumerate(ballList):
        plot.plotPoint(i, ball.Loc.x, ball.Loc.y)
    
    brakeAzmuth = math.atan2(ballList[1].Loc.y - ballList[0].Loc.y, ballList[1].Loc.x - ballList[0].Loc.x)
    
    brake = tableballdefs.Shot(ballList[0], 2.75, brakeAzmuth)
    brake.execute()
    ballsMoving = True
    timeStep = 0.01
    stopVel = 0.05
    elapsedTime = 0
    
    
    while ballsMoving :
        countStoppedBalls = 0
        for k, ball in enumerate(ballList): 
            
            if ball.Vel.getLength() <= stopVel: 
                ball.zeroVel()
                countStoppedBalls = countStoppedBalls + 1
                
                    
            else:
                ballsMoving = True
                #check to see if the ball has hit a wall, if so reverse the velocity dir
                if ball.Loc.x + ball.diameter/2 >= table.length or ball.Loc.x - ball.diameter/2 <= 0 : 
                    ball.Vel.x = -1 * table.cushionBounce * ball.Vel.x
                if ball.Loc.y + ball.diameter/2 >= table.width or ball.Loc.y - ball.diameter/2 <= 0 : 
                    ball.Vel.y = -1 * table.cushionBounce * ball.Vel.y
                
                #update the ball velocity from the acceleration
                ball.Loc.x = ball.Loc.x + (ball.Vel.x * timeStep)
                ball.Loc.y = ball.Loc.y + (ball.Vel.y * timeStep)
                plot.plotPoint(k, ball.Loc.x, ball.Loc.y)
                
                radius = ball.diameter / 2
                
                #calculate the acceleration based on the table and ball conditions
                acc = -(2*9.8*table.feltThickness)/(3*radius*radius)
                
                alpha = math.atan2(ball.Vel.y,ball.Vel.x)
                
                xAcc = math.cos(alpha) * acc
                yAcc = math.sin(alpha) * acc
                
                ball.Vel.x = ball.Vel.x + (xAcc * timeStep)
                ball.Vel.y = ball.Vel.y + (yAcc * timeStep)
                 
        for ball1, ball2 in itertools.combinations(ballList, 2):
             if collision.happened(ball1, ball2) : collision.run(ball1, ball2)
            
        if countStoppedBalls == numBalls : ballsMoving = False
        elapsedTime = elapsedTime + timeStep
        
    
            
    return      
            

if __name__ == "__main__":
    main()