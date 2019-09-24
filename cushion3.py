# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs
import spin
import simulation
import math

def rail_bounce(mass, init_vel, spring_coef, damper_coef):
    x = 0
    positive = init_vel > 0
    vel = math.fabs(init_vel)
    ts = 0.001
    max_x = 0
    while x >= 0:
        acc = -((spring_coef * x) + (damper_coef * vel)) / mass
        vel += acc * ts
        x += vel * ts
        if x > max_x: max_x = x
    return vel if positive else -vel


def Carom(ball, table, timeStep):
    
    rightRail = ball.Loc.x + ball.radius + table.cushionThickness >= table.length
    leftRail = ball.Loc.x - ball.radius - table.cushionThickness <= 0
    topRail = ball.Loc.y + ball.radius + table.cushionThickness >= table.width
    bottomRail = ball.Loc.y - ball.radius - table.cushionThickness <= 0
    
    # checking to see if the ball is near a pocket.
    pocketProcsimity  = 2 * table.pocketRadius * math.sin(math.radians(45)) + \
                        table.cushionThickness / math.tan(table.cornerPocketAngle) + \
                        table.cornerRadius
    
    for pocket in table.pocketList:
        if math.hypot(pocket.Loc.x - ball.Loc.x, pocket.Loc.y - ball.Loc.y) <= pocketProcsimity:
            ball.pocket()
            print("ball pocketed")
            return
    
    # this is an attempt to fix the carom algorithm,
    # there is a problem with the physics in that the carom may take longer than one timeStep,
    # a calc needs to be added to account for the time spent in contact with the rail.
    # I think a mass spring damper type system needs to be implemented.
    if rightRail or leftRail:
        x = ball.Loc.x + ball.radius + table.cushionThickness - table.length if \
            rightRail else ball.Loc.x - ball.radius - table.cushionThickness
        acc_x = -((table.cushion_spring_coef * x) + (table.cushion_damper_coef * ball.Vel.x)) / ball.mass
        ball.Vel.x += acc_x * timeStep
        ball.Loc.x += ball.Vel.x * timeStep

        normal = ball.mass * acc_x
        ffy_ = ball.Vel.y + ball.spinZ * ball.radius > 0 if rightRail else ball.Vel.y - ball.spinZ * ball.radius > 0
        friction_force_y = spin.SolveFF(table.feltFrictionCo, normal)
        alpha_z = spin.SolveAlpha(ball.radius, ball.momentOfInertia, friction_force_y)

        if spin.DidBallGrip(ball.Vel.y, alpha_z, timeStep, ball.spinZ, ball.radius):
            ball.spinZ = ball.Vel.y / ball.radius
        else:
            ball.spinZ += alpha_z * timeStep
            acc_y = friction_force_y / ball.mass
            ball.Vel.y += acc_y * timeStep

    if topRail or bottomRail:
        y = ball.Loc.y + ball.radius + table.cushionThickness - table.width
        acc_y = ((table.cushion_spring_coef * y) + (table.cushion_damper_coef * ball.Vel.y)) / ball.mass
        if topRail: acc_y *= -1
        ball.Vel.y += acc_y * timeStep
        ball.Loc.y += ball.Vel.y * timeStep

        # normal = ball.mass * acc_y
        # friction_force_x = normal * table.feltFrictionCo
        # alpha_z = spin.SolveAlpha(ball.mass, ball.radius, ball.momentOfInertia, table.feltFrictionCo, normal)


if __name__ == "__main__":
    
    table = tableballdefs.Table(9, 0.000025, 0.08)
    ball = tableballdefs.Ball(0, 0, table.length*0.25, table.width*0.75, 0, 0, 0)
    shot = tableballdefs.Shot(ball, 1.5, math.radians(180), ball.radius / -2, 0)
    ballList = [ball]

    sim = simulation.Simulation(1, ballList, shot, table)
    sim.run()
