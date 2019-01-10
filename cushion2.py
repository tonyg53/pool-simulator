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
            print("ball near pocket")
    
    #this is an attempt to fix the carom algorithm, seems to work, should test it locally
    if rightRail or leftRail:
        prevXvel = ball.Vel.x
        ball.Vel.x *= -1 * table.cushionBounce
        ball.Loc.x = table.length - table.cushionThickness - ball.radius if rightRail else table.cushionThickness + ball.radius
        accX = prevXvel - ball.Vel.x / timeStep
        normalF = ball.mass * accX
        ffy = normalF * table.feltFrictionCo
        alphaZ = spin.SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo, normalF)
        if spin.DidBallGrip(ball.Vel.y, alphaZ, timeStep, ball.spinZ, ball.radius):
            ball.spinZ = ball.Vel.y / ball.radius
            if rightRail: ball.spinZ *= -1
            return
        if leftRail and ball.Vel.y > ball.spinZ * ball.radius: ffy *= -1
        if rightRail and ball.Vel.y < ball.spinZ * ball.radius: ffy *= -1
        if leftRail and ball.Vel.y < ball.spinZ * ball.radius: alphaZ *= -1
        if rightRail and ball.Vel.y > ball.spinZ * ball.radius: alphaZ *= -1
        
        
        ball.spinZ += alphaZ * timeStep
        accY = ffy/ball.mass
        ball.Vel.y += accY * timeStep
        
    
    elif topRail or bottomRail:
        prevYvel = ball.Vel.y
        ball.Vel.y *= -1 * table.cushionBounce
        ball.Loc.y = table.width - table.cushionThickness - ball.radius if topRail else table.cushionThickness + ball.radius
        accY = prevYvel - ball.Vel.y / timeStep
        normalF = ball.mass * accY
        ffx = normalF * table.feltFrictionCo
        alphaZ = spin.SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo, normalF)
        if spin.DidBallGrip(ball.Vel.x, alphaZ, timeStep, ball.spinZ, ball.radius):
            ball.SpinZ = ball.Vel.x / ball.radius
            if bottomRail: ball.SpinZ *= -1
            return
        
        if topRail and ball.Vel.x > ball.spinZ * ball.radius: ffx *= -1
        if bottomRail and ball.Vel.x < ball.spinZ * ball.radius: ffx *= -1
        if topRail and ball.Vel.x < ball.spinZ * ball.radius: alphaZ *= -1
        if bottomRail and ball.Vel.x > ball.spinZ * ball.radius: alphaZ *= -1
        
        ball.spinZ += alphaZ * timeStep
        accX = ffx/ball.mass
        ball.Vel.x += accX * timeStep

if __name__ == "__main__":
    
    table = tableballdefs.Table(9, 0.000025, 0.3)
    ball = tableballdefs.Ball(0,0,table.length*0.75,table.width*0.75,0,0,0)
    shot = tableballdefs.Shot(ball, 1, math.radians(15))
    ballList = []
    ballList.append(ball)
    
    sim = simulation.Simulation(1,ballList,shot,table)
    sim.run()