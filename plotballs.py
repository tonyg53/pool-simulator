# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:08:10 2018

@author: tony.gold
"""
import matplotlib.pyplot as plt
import tableballdefs

class PlotBalls(object):
    
    def __init__(self, numBalls=1, table = tableballdefs.Table()):
        self.table = table
        self.markerList = ['ko', 'yo', 'bo', 'ro', 'mo', 'co', 'go']
        if numBalls > len(self.markerList): raise "too many balls to plot"
        v = [0, self.table.length, 0, self.table.width]
        plt.axis(v)
        
    def plotPoint(self, ballNum, x, y):
        plt.plot(x, y, self.markerList[ballNum])
        
    def showPlot(self):
        plt.show()
        

            
    