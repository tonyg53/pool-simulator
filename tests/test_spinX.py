from unittest import TestCase
import tableballdefs as defs
import spin


class TestSpinX(TestCase):
    def test_RollRight(self):
        ball = defs.Ball(2)
        xSpin = ball.Vel.x / ball.radius
        ball.spinX = xSpin
        table = defs.Table()
        timeStep = 0.001

        friction_force = spin.SpinX(ball, table.feltFrictionCo, timeStep)
        self.assertEqual(ball.spinX, xSpin, msg="ball spin should be the same as velocity has not changed")
        self.assertEqual(friction_force, 0, msg="friction force due to sliding should be zero")
