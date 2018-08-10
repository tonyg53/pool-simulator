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
    
    def __init__(self, length = 9, feltThickness = 0.000025, feltFrictionCo = 0.01, cushionBounce = 0.9):
        #convert feet to meters
        self.length = length * 0.3048
        #standard table width is half the length then convert to meters
        self.width = (length / 2) * 0.3048
        self.feltThickness = feltThickness
        self.feltFrictionCo = feltFrictionCo
        self.cushionBounce = cushionBounce

class Ball(object):
    
    def __init__(self, xVel = 0, yVel = 0, xLoc = 0, yLoc = 0, english = 0, topSpin = 0):
        self.radius = 0.0286
        self.mass = 0.165
        self.elasticity = 0.99
        self.Vel = Vector(xVel,yVel)
        self.Loc = Vector(xLoc,yLoc)
        self.english = english
        self.topSpin = topSpin
        self.momentOfInertia = (2/5)*self.mass*self.radius*self.radius
        
    def zeroVel(self):
        self.Vel = Vector(0,0)
        
class CueStick(object):
    
    def __init__(self, mass = 20, COR = 0.98):
        self.mass = mass * 0.0283495
        self.COR = COR
        
class Shot(object):
    
    def __init__(self, cueBall, cueStickVelocity = 2, shotAzmuth = 0, strikePtX = 0, strikePtY = 0, cueStick = CueStick()):
        
        self.cueStickVelocity = cueStickVelocity
        self.strikePtX = strikePtX
        self.strikePtY = strikePtY
        self.shotAzmuth = shotAzmuth
        self.cueBall = cueBall
        self.cueStick = cueStick
        
    def execute(self):
        if self.cueBall.Vel.getLength() != 0 : raise "wait for balls to stop"

        #assume stick is accelerated for 0.5 sec
        stickForce = self.cueStick.mass * self.cueStickVelocity / 0.5
        #assume stick force is applied to the ball for 0.1 sec
        ballVel = stickForce * 0.1 / self.cueBall.mass
        
        #strikePtY is the distance above or below center and strikePtX is the distance left or right of center
        self.cueBall.topSpin = self.strikePtY * stickForce * 0.1 / self.cueBall.momentOfInertia
        self.cueBall.english = self.strikePtX * stickForce * 0.1 / self.cueBall.momentOfInertia
        self.cueBall.Vel.x = math.cos(self.shotAzmuth)*ballVel
        self.cueBall.Vel.y = math.sin(self.shotAzmuth)*ballVel
        return self.cueBall


      
    
