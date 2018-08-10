# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 12:34:13 2018

@author: tony.gold
"""

import simulation
import tableballdefs

import math
import random

class Setup(object):
    
    def __init__(self, numballs = 4, ballList = [], table = tableballdefs.Table()):
        self.numballs = numballs
        self.table = table
        self.ballList = Rack(numballs, table)

    def SetupSim(self):
                
        brakeAzmuth = math.atan2(self.ballList[1].Loc.y - self.ballList[0].Loc.y, self.ballList[1].Loc.x - self.ballList[0].Loc.x)
        shot = tableballdefs.Shot(self.ballList[0], 2, brakeAzmuth, 0, self.ballList[0].radius/2)
        sim = simulation.Simulation(self.numballs, self.ballList, shot, self.table)
        sim.run()
    
def Rack(numBalls, table):
    ballList = []
    
    for i in range(0, numBalls):
        ballList.append(tableballdefs.Ball())
    
    if len(ballList) == 4:
        ballList[0].Loc.x = table.length / 4
        ballList[0].Loc.y = table.width / 2
        ballList[1].Loc.x = table.length * 3 / 4
        ballList[1].Loc.y = table.width / 2
        ballList[2].Loc.x = ballList[1].Loc.x + random.random()/100 + math.cos(math.radians(60))*ballList[1].radius
        ballList[2].Loc.y = ballList[1].Loc.y + math.sin(math.radians(60))*ballList[1].radius
        ballList[3].Loc.x = ballList[1].Loc.x + math.cos(math.radians(60))*ballList[1].radius
        ballList[3].Loc.y = ballList[1].Loc.y - random.random()/100 - math.sin(math.radians(60))*ballList[1].radius
        
    return ballList
    
if __name__ == "__main__":
    setup = Setup()
    setup.SetupSim()