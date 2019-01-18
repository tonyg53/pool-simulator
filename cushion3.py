# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs
import spin
import simulation
import math

def Carom(ball, table, timeStep):
    
    rightRail = ball.Loc.x + ball.radius + table.cushionThickness >= table.length
    leftRail = ball.Loc.x - ball.radius - table.cushionThickness <= 0
    topRail = ball.Loc.y + ball.radius + table.cushionThickness >= table.width
    bottomRail = ball.Loc.y - ball.radius - table.cushionThickness <= 0
    
    #checking to see if the ball is near a pocket.
    pocketProcsimity  = 2 * table.pocketRadius * math.sin(math.radians(45)) + table.cushionThickness / math.tan(table.cornerPocketAngle) + table.cornerRadius
    
    for pocket in table.pocketList:
        if math.hypot(pocket.Loc.x - ball.Loc.x, pocket.Loc.y - ball.Loc.y) <= pocketProcsimity:
            ball.pocket()
            print("ball pocketed")
    
    #this is an attempt to fix the carom algorithm, seems to work, should test it locally
    #there is a problem with the physics in that the carom may take longer than one timeStep, 
    #a calc needs to be added to account for the time spent in contact with the rail.
    if rightRail:
        prevXvel = ball.Vel.x
        ball.Vel.x *= -1 * table.cushionBounce
        ball.Loc.x = table.length - table.cushionThickness - ball.radius
        accX = ball.Vel.x - prevXvel / timeStep
        normalF = ball.mass * accX
        ffY = abs(normalF * table.feltFrictionCo)
        alphaZ = spin.SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo, normalF)
        if spin.DidBallGrip(ball.Vel.y, alphaZ, timeStep, ball.spinZ, ball.radius):
            

if __name__ == "__main__":
    
    table = tableballdefs.Table(9, 0.000025, 0.3)
    ball = tableballdefs.Ball(0,0,table.length*0.75,table.width*0.75,0,0,0)
    shot = tableballdefs.Shot(ball, 1.25, math.radians(15))
    ballList = []
    ballList.append(ball)
    
    sim = simulation.Simulation(1,ballList,shot,table)
    sim.run()