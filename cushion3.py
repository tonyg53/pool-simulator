# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:36:11 2018

@author: tony.gold
"""
import tableballdefs
from spin import Rail
import spin
import simulation
import math


def generic_rail_bounce(z_spin, perpindicular_v, cushion_deflection, parrallel_v, springCoef, damperCoef, frictionCoef, timeStep):
    """
    Calculates the velocity of the ball assuming that the ball is hitting the Left rail
    This allows for a positive parrallel velocity imparting a positive z spin on the ball.
    | <-- o
    sign convention for other rails should be converted on input parameters.
    """
    b = tableballdefs.Ball(perpindicular_v, parrallel_v, cushion_deflection, 0, 0, 0, z_spin)

    acc = -((springCoef * cushion_deflection) + (damperCoef * perpindicular_v)) / b.mass
    perpindicular_v += acc * timeStep
    cushion_deflection += perpindicular_v * timeStep

    normal = b.mass * acc
    ff_parrellel = spin.SpinZ(b, frictionCoef, normal, timeStep)
    acc_para = ff_parrellel / b.mass
    parrallel_v += acc_para * timeStep

    return [perpindicular_v, cushion_deflection, parrallel_v, b.spinZ]


def Carom(ball, table, timeStep):
    # checking to see if the ball is near a pocket.
    pocketProcsimity = 2 * table.pocketRadius * math.sin(math.radians(45)) + \
                       table.cushionThickness / math.tan(table.cornerPocketAngle) + \
                       table.cornerRadius

    for pocket in table.pocketList:
        if math.hypot(pocket.Loc.x - ball.Loc.x, pocket.Loc.y - ball.Loc.y) <= pocketProcsimity:
            ball.pocket()
            print("ball pocketed")
            return
    
    if ball.Loc.x + ball.radius + table.cushionThickness >= table.length:
        x = table.length - (ball.Loc.x + ball.radius + table.cushionThickness)
        x_vel, x, y_vel, ball.spinZ = generic_rail_bounce(ball.spinZ,
                                                          -ball.Vel.x,
                                                          x,
                                                          -ball.Vel.y,
                                                          table.cushion_spring_coef,
                                                          table.cushion_damper_coef,
                                                          table.feltFrictionCo,
                                                          timeStep)
        ball.Vel.x = -x_vel
        ball.Vel.y = -y_vel
    elif ball.Loc.x - ball.radius - table.cushionThickness <= 0:
        x = ball.Loc.x - ball.radius - table.cushionThickness
        ball.Vel.x, x, ball.Vel.y, ball.spinZ = generic_rail_bounce(ball.spinZ,
                                                                    ball.Vel.x,
                                                                    x,
                                                                    ball.Vel.y,
                                                                    table.cushion_spring_coef,
                                                                    table.cushion_damper_coef,
                                                                    table.feltFrictionCo,
                                                                    timeStep)
    elif ball.Loc.y + ball.radius + table.cushionThickness >= table.width:
        y = table.width - (ball.Loc.y + ball.radius + table.cushionThickness)
        y_vel, y, ball.Vel.x, ball.spinZ = generic_rail_bounce(ball.spinZ,
                                                          -ball.Vel.y,
                                                          y,
                                                          ball.Vel.x,
                                                          table.cushion_spring_coef,
                                                          table.cushion_damper_coef,
                                                          table.feltFrictionCo,
                                                          timeStep)
        ball.Vel.y = -y_vel
    elif ball.Loc.y - ball.radius - table.cushionThickness <= 0:
        y = ball.Loc.y - ball.radius - table.cushionThickness
        ball.Vel.y, y, xVel, ball.spinZ = generic_rail_bounce(ball.spinZ,
                                                              ball.Vel.y,
                                                              y,
                                                              -ball.Vel.x,
                                                              table.cushion_spring_coef,
                                                              table.cushion_damper_coef,
                                                              table.feltFrictionCo,
                                                              timeStep)
        ball.Vel.x = -xVel
    else:
        return
    



if __name__ == "__main__":
    
    table = tableballdefs.Table(9, 0.000025, 0.08)
    ball = tableballdefs.Ball(0, 0, table.length*0.25, table.width*0.75, 0, 0, 0)
    shot = tableballdefs.Shot(ball, 1.5, math.radians(165), 0, 0)
    ballList = [ball]

    sim = simulation.Simulation(1, ballList, shot, table)
    sim.run()
