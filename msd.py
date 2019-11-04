"""
Created on Tue May 28 2019
@author: tony.gold
"""
import math


def rail_bounce(mass, init_vel, spring_coef, damper_coef):
    x = 0.00001
    positive = init_vel > 0
    vel = math.fabs(init_vel)
    ts = 0.001
    max_x = 0
    while x >= 0:
        acc = -((spring_coef * x) + (damper_coef * vel)) / mass
        vel += acc * ts
        x += vel * ts
        if x > max_x: max_x = x
    print(max_x)
    return vel if positive else -vel


if __name__ == "__main__":
    exit_vel = rail_bounce(0.165, 2, 17500, 2.5)
    print(exit_vel)