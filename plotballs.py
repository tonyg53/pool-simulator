# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:08:10 2018

@author: tony.gold
"""
import matplotlib.pyplot as plt

class PlotBalls(object):
    
    def __init__(self, numBalls=1):
        self.markerList = ['ro', 'bo', 'go', 'mo']
        if numBalls > len(self.markerList): raise "too many balls to plot"
        
    def plotPoint(self, ballNum, x, y):
        plt.plot(x, y, self.markerList[ballNum])
        
    def showPlot(self):
        plt.show()
        

            
    