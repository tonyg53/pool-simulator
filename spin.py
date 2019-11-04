# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:47:40 2018

@author: tony.gold
"""

from enum import Enum


# returns the friction force due to the ball sliding,
# returns 0 if the ball is spinning at the same velocity as it's moving
def SpinX(ball, frictionCoef, timeStep):
    normal = 9.8 * ball.mass
    ff = SolveFF(frictionCoef, normal)
    alpha = SolveAlpha(ball.radius, ball.momentOfInertia, ff)
    
    if DidBallGrip(ball.Vel.y, alpha, timeStep, ball.spinX, ball.radius):
        ball.spinX = -ball.Vel.y / ball.radius
        return 0

    edge_vel = ball.Vel.y + (ball.spinX * ball.radius)

    if edge_vel > 0:
        ff *= -1
        alpha *= -1

    ball.spinX += alpha * timeStep
    return ff


# returns the friction force due to the ball sliding,
# returns 0 if the ball is spinning at the same velocity as it's moving
def SpinY(ball, frictionCoef, timeStep):
    normal = 9.8 * ball.mass
    ff = SolveFF(frictionCoef, normal)
    alpha = SolveAlpha(ball.radius, ball.momentOfInertia, ff)

    if DidBallGrip(ball.Vel.x, alpha, timeStep, ball.spinY, ball.radius):
        ball.spinY = ball.Vel.x / ball.radius
        return 0

    edge_vel = ball.Vel.x - (ball.spinY * ball.radius)

    if edge_vel > 0:
        ff *= -1
    elif edge_vel < 0:
        alpha *= -1

    ball.spinY += alpha * timeStep
    return ff

def SpinZ(ball, frictionCoef, normal, timeStep):
    """
    Calculates the z spin and resultant friction force of the ball assuming that the ball is hitting the Left rail
    This allows for a positive parrallel velocity imparting a positive z spin on the ball.
    | <-- o
    sign convention for other rails should be converted on input parameters.
    """
    ff = SolveFF(frictionCoef, normal)
    alpha = -SolveAlpha(ball.radius, ball.momentOfInertia, ff)

    if DidBallGrip(ball.Vel.y, alpha, timeStep, ball.spinZ, ball.radius):
        ball.spinZ = ball.Vel.y / ball.radius
        return 0
    ball.spinZ += alpha * timeStep
    edge_v = ball.Vel.y - (ball.spinZ * ball.radius)
    if edge_v > 0:
        ff *= -1

    return ff

    
def SolveAlpha(radius, moi, ff):
    torqueFF = ff * radius
    return torqueFF / moi


def SolveFF(frictionCo, normalForce):
    return normalForce * frictionCo


def DidBallGrip(vel, alpha, timeStep, omega, radius):
    if round(abs(abs(omega) - abs(alpha * timeStep)) * radius,1) == round(abs(vel), 1):
        return True
    return False

class Rail(Enum):
    RIGHT = 1
    LEFT = 2
    TOP = 3
    BOTTOM = 4
