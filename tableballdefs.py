# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:35:15 2018

@author: tony.gold
"""
import math

class Vector(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getLength(self):
        return math.hypot(self.x,self.y)

class Table(object):
    
    def __init__(self, length = 9, feltThickness = 0.00005, feltFrictionCo = 0.1, cushionBounce = 0.9):
        self.length = length * 0.3048
        self.width = (length / 2) * 0.3048
        self.feltThickness = feltThickness
        self.feltFrictionCo = feltFrictionCo
        self.cushionBounce = cushionBounce

class Ball(object):
    
    def __init__(self, xVel = 0, yVel = 0, diameter = 0.0572, mass = 0.165, elasticity = 0.99, xLoc = 0, yLoc = 0, english = 0, topSpin = 0):
        self.diameter = diameter
        self.mass = mass
        self.elasticity = elasticity
        self.Vel = Vector(xVel,yVel)
        self.Loc = Vector(xLoc,yLoc)
        self.english = english
        self.topSpin = topSpin
        
    def zeroVel(self):
        self.Vel = Vector(0,0)
        
class Shot(object):
    
    def __init__(self, cueBall, cueStickVelocity = 2, shotAzmuth = 0, cueStickMass = 20, cueStickCOR = 0.98, strikePtDistFromCenter = 0, strikePtAngle = 0):
        self.cueStickMass = cueStickMass * 0.0283495
        self.cueStickVelocity = cueStickVelocity
        self.cueStickCOR = cueStickCOR
        self.strikePtDistFromCenter = strikePtDistFromCenter
        self.strikePtAngle = strikePtAngle
        self.shotAzmuth = shotAzmuth
        self.cueBall = cueBall
        
    def execute(self):
        if self.cueBall.Vel.length != 0 : raise "wait for balls to stop"

        stickForce = self.cueStickMass * self.cueStickVelocity
        ballVel = stickForce/(self.cueBall.mass + self.cueStickMass)
        self.cueBall.Vel.x = math.cos(math.radians(self.shotAzmuth))*ballVel
        self.cueBall.Vel.y = math.sin(math.radians(self.shotAzmuth))*ballVel
        return self.cueBall


      
    
