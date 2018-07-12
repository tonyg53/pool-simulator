# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:35:15 2018

@author: tony.gold
"""
import math

class Table(object):
    
    def __init__(self, length = 9, feltThickness = 0.000005, feltFrictionCo = 0.1, cushionBounce = 0.65):
        self.length = length * 0.3048
        self.width = (length / 2) * 0.3048
        self.feltThickness = feltThickness
        self.feltFrictionCo = feltFrictionCo
        self.cushionBounce = cushionBounce

class Ball(object):
    
    def __init__(self, xVel = 0, yVel=0, diameter = 0.0572, mass = 0.165, elasticity = 0.99, xLoc = 0, yLoc = 0, english = 0, topSpin = 0):
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
    
    def __init__(self, cueBall, cueStickVelocity = 2, shotAzmuth = 0, cueStickMass = 20, cueStickCOR = 0.85, strikePtDistFromCenter = 0, strikePtAngle = 0):
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
      
    
