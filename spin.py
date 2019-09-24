# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:47:40 2018

@author: tony.gold
"""

import tableballdefs


def Test():
    ball = tableballdefs.Ball(2, -2, 0, 0, 30, -30)
    table = tableballdefs.Table()
    timeStep = 0.001

    frictionForceY = SpinX(ball, table, timeStep)
    frictionForceX = SpinY(ball, table, timeStep)

    time = timeStep

    while frictionForceY != 0 or frictionForceX != 0:


        acc_x_ff = frictionForceX / ball.mass
        acc_y_ff = frictionForceY / ball.mass

        ball.Vel.x += acc_x_ff * timeStep
        ball.Vel.y += acc_y_ff * timeStep

        frictionForceY = SpinX(ball, table, timeStep)
        frictionForceX = SpinY(ball, table, timeStep)

        print("Vel x: ", ball.Vel.x, "Vel y: ", ball.Vel.y,
              "Spin x: ", ball.spinX * ball.radius, "Spin y: ", ball.spinY * ball.radius,
              "Elapsed time: ", time)
        time += timeStep


# returns the friction force due to the ball sliding,
# returns 0 if the ball is spinning at the same velocity as it's moving
def SpinX(ball, table, timeStep):
    normal = 9.8 * ball.mass
    ff_dir = ball.Vel.y + (ball.spinX * ball.radius) < 0
    ff = SolveFF(table.feltFrictionCo, normal, ff_dir) if ball.Vel.y != 0 else 0
    alpha = SolveAlpha(ball.radius, ball.momentOfInertia, ff)
    
    if DidBallGrip(ball.Vel.y, alpha, timeStep, ball.spinX, ball.radius):
        ball.spinX = -1 * ball.Vel.y / ball.radius
        return 0

    ball.spinX += alpha * timeStep
    return ff


# returns the friction force due to the ball sliding,
# returns 0 if the ball is spinning at the same velocity as it's moving
def SpinY(ball, table, timeStep):
    normal = 9.8 * ball.mass
    ff_dir = ball.Vel.x - (ball.spinY * ball.radius) < 0
    ff = SolveFF(table.feltFrictionCo, normal, ff_dir) if ball.Vel.x != 0 else 0
    alpha = -SolveAlpha(ball.radius, ball.momentOfInertia, ff)

    if DidBallGrip(ball.Vel.x, alpha, timeStep, ball.spinY, ball.radius):
        ball.spinY = ball.Vel.x / ball.radius
        return 0

    ball.spinY += alpha * timeStep
    return ff

    
def SolveAlpha(radius, moi, ff):
    torqueFF = ff * radius
    return torqueFF / moi


def SolveFF(frictionCo, normalForce):
    return normalForce * frictionCo


def DidBallGrip(vel, alpha, timeStep, omega, radius):
    if round(abs(abs(omega) - abs(alpha * timeStep)) * radius,2) == round(abs(vel), 2):
        return True
    return False


if __name__ == "__main__":
    Test()
