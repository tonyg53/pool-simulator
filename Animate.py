"""
author: tony.gold
date: 15/10/2019
"""

from tkinter import *
import tableballdefs as defs
import time

class Window(object):

    def __init__(self, numBalls, table):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=table.length * 400, height=table.width * 400)
        self.canvas.bind('ball_moved', self.move_ball())
        self.canvas.pack()

        self.ball_list = []
        for i in range(0,numBalls):
            ball = self.canvas.create_oval(0, 0, 10, 10)
            self.ball_list.append(ball)


    def move_ball(self, ballNum, x, y):
        ball = self.ball_list[ballNum]
        cur_pos = self.canvas.coords(ball)

        self.canvas.move(ball, cur_pos[2]+x, cur_pos[3]+y)



if __name__ == "__main__":
    t = defs.Table()
    w = Window(1, t)
    w.tk.mainloop()

