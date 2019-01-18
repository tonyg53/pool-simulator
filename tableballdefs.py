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
    
    def __init__(self, 
                 length = 9, 
                 feltThickness = 0.000025, 
                 feltFrictionCo = 0.3, 
                 cushionBounce = 0.9, 
                 cushionThickness = 0.051, 
                 pocketRadius = 0.0536, 
                 cornerRadius = 0.005, 
                 cornerPocketAngle = 45, 
                 sidePocketAngle = 85):
        #convert feet to meters
        self.length = length * 0.3048
        #standard table width is half the length then convert to meters
        self.width = (length / 2) * 0.3048
        self.feltThickness = feltThickness
        self.feltFrictionCo = feltFrictionCo
        self.cushionBounce = cushionBounce
        self.cushionThickness = cushionThickness
        self.pocketRadius = pocketRadius
        self.cornerRadius = cornerRadius
        self.cornerPocketAngle = cornerPocketAngle
        self.sidePocketAngle = sidePocketAngle
        
        self.cornerPocketDepth = (self.cushionThickness / math.tan(math.radians(45))) + (
                2 * self.pocketRadius * math.sin(math.radians(self.cornerPocketAngle))) - self.cushionThickness
                
        pocketLocationFactor = self.pocketRadius * math.sin(math.radians(45))
        self.pocketList = []
        p = Pocket(self.pocketRadius,
                   self.cornerPocketAngle, 
                   self.cornerRadius, 
                   self.cushionThickness, 
                   pocketLocationFactor, 
                   pocketLocationFactor)
        
        self.pocketList.append(p)
        
        p = Pocket(self.pocketRadius,
                   self.cornerPocketAngle, 
                   self.cornerRadius, 
                   self.cushionThickness, 
                   pocketLocationFactor, 
                   self.width - pocketLocationFactor)
        
        self.pocketList.append(p)
        
        p = Pocket(self.pocketRadius,
                   self.cornerPocketAngle, 
                   self.cornerRadius, 
                   self.cushionThickness, 
                   self.length - pocketLocationFactor, 
                   self.width - pocketLocationFactor)
        
        self.pocketList.append(p)
        
        p = Pocket(self.pocketRadius,
                   self.cornerPocketAngle, 
                   self.cornerRadius, 
                   self.cushionThickness, 
                   self.length - pocketLocationFactor, 
                   pocketLocationFactor)
        
        self.pocketList.append(p)
        
        p = Pocket(self.pocketRadius, 
                                self.sidePocketAngle, 
                                self.cornerRadius, 
                                self.cushionThickness,
                                self.length / 2,
                                0)
        
        self.pocketList.append(p)
        
        p = Pocket(self.pocketRadius, 
                                self.sidePocketAngle, 
                                self.cornerRadius, 
                                self.cushionThickness,
                                self.length / 2,
                                self.width)
        
        self.pocketList.append(p)
        
class Pocket(object):
    
    def __init__(self, radius, cushionAngle, cornerRadius, cushionThickness, xLoc, yLoc):
        self.radius = radius
        self.cushionAngle = cushionAngle
        self.cornerRadius = cornerRadius
        self.cushionThickness = cushionThickness
        self.Loc = Vector(xLoc, yLoc)
        

class Ball(object):
    
    def __init__(self, xVel = 0, yVel = 0, xLoc = 0, yLoc = 0, spinX = 0, spinY = 0, spinZ = 0):
        self.radius = 0.0286
        self.mass = 0.165
        self.elasticity = 0.99
        self.Vel = Vector(xVel,yVel)
        self.Loc = Vector(xLoc,yLoc)
        self.spinX = spinX
        self.spinY = spinY
        self.spinZ = spinZ
        self.momentOfInertia = (2/5)*self.mass*self.radius*self.radius
        self.pocketed = False
        
    def zeroVel(self):
        self.Vel = Vector(0,0)
        self.spinX = 0
        self.spinY = 0
        self.spinZ = 0
        
    def pocket(self):
        self.pocketed = True
        self.zeroVel()
        
        
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
        
    def didMisscue(self):
        strikeMomentArm = math.sqrt(math.pow(self.strikePtX,2)+math.pow(self.strikePtY,2))
        
        if strikeMomentArm > self.cueBall.radius/2 : 
            print("misscue")
            return True
        
        return False
        
    def execute(self):
        if self.cueBall.Vel.getLength() != 0 : raise "wait for balls to stop"

        #assume stick is accelerated for 0.5 sec
        stickForce = self.cueStick.mass * self.cueStickVelocity / 0.5
        
        self.didMisscue()
        
        #assume stick force is applied to the ball for 0.1 sec
        ballVel = stickForce * 0.1 / self.cueBall.mass
        
        #strikePtY is the distance above or below center and strikePtX is the distance left or right of center
        topSpin = self.strikePtY * stickForce * 0.1 / self.cueBall.momentOfInertia
        
        self.cueBall.spinX = topSpin * math.sin(self.shotAzmuth)
        self.cueBall.spinY = topSpin * math.cos(self.shotAzmuth)
        self.cueBall.spinZ = self.strikePtX * stickForce * 0.1 / self.cueBall.momentOfInertia
        self.cueBall.Vel.x = math.cos(self.shotAzmuth) * ballVel
        self.cueBall.Vel.y = math.sin(self.shotAzmuth) * ballVel
        return self.cueBall


      
    
