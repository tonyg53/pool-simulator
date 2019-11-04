import tableballdefs as defs
import spin


def Test():
    ball = defs.Ball()
    table = defs.Table()
    timeStep = 0.001

    print(test_roll_right(ball, table.feltFrictionCo, timeStep))
    print(test_slide_right(ball, table.feltFrictionCo, timeStep))
    print(test_skid_right(ball, table.feltFrictionCo, timeStep))
    print(test_roll_left(ball, table.feltFrictionCo, timeStep))
    print(test_slide_left(ball, table.feltFrictionCo, timeStep))
    print(test_skid_left(ball, table.feltFrictionCo, timeStep))
    print(test_roll_up(ball, table.feltFrictionCo, timeStep))
    print(test_slide_up(ball, table.feltFrictionCo, timeStep))
    print(test_skid_up(ball, table.feltFrictionCo, timeStep))
    print(test_roll_down(ball, table.feltFrictionCo, timeStep))
    print(test_slide_down(ball, table.feltFrictionCo, timeStep))
    print(test_skid_down(ball, table.feltFrictionCo, timeStep))


def test_roll_right(ball, friction, time):
    ball.Vel.x = 2
    ySpin = ball.Vel.x / ball.radius
    ball.spinY = ySpin

    friction_force_x = spin.SpinY(ball, friction, time)
    msg = ""
    if ball.spinY != ySpin:
        msg += "y spin should not have changed ball is rolling right, "
    if friction_force_x != 0:
        msg += "x friction force should be 0 ball is rolling right, "
    if msg == "": return "x rolling right test passed"
    return msg


def test_slide_right(ball, friction, time):
    ball.Vel.x = 2
    ySpin = 0
    ball.spinY = ySpin

    friction_force_x = spin.SpinY(ball, friction, time)
    msg = ""
    if friction_force_x >= 0:
        msg += "x friction force should be negative ball is sliding right, "
    if ball.spinY <= ySpin:
        msg += "y spin should have increased ball is sliding right, "
    if msg == "": return "x sliding right test passed"
    return msg

def test_skid_right(ball, friction, time):
    ball.Vel.x = 0
    ySpin = -2 / ball.radius
    ball.spinY = ySpin

    friction_force_x = spin.SpinY(ball, friction, time)
    msg = ""
    if friction_force_x >= 0:
        msg +=" x friction force should be negative ball is skidding right, "
    if ball.spinY <= ySpin:
        msg += "y spin should have decreased ball is skidding right, "
    if msg == "": return "x skidding right test passed"
    return msg


def test_roll_left(ball, friction, time):
    ball.Vel.x = -2
    ySpin = ball.Vel.x / ball.radius
    ball.spinY = ySpin

    friction_force_x = spin.SpinY(ball, friction, time)
    msg = ""
    if friction_force_x != 0:
        msg += "x friction force should be zero ball is rolling left, "
    if ball.spinY != ySpin:
        msg += "y spin should not have changed ball is rolling left, "
    if msg == "": return "x rolling left test passed"
    return msg


def test_slide_left(ball, friction, time):
    ball.Vel.x = -2
    ySpin = 0
    ball.spinY = ySpin

    friction_force_x = spin.SpinY(ball, friction, time)
    msg = ""
    if friction_force_x <= 0:
        msg += "x friction force should be positive ball is sliding left, "
    if ball.spinY >= ySpin:
        msg += "y spin should have decreased ball is sliding left, "
    if msg == "": return "x sliding left test passed"
    return msg

def test_skid_left(ball, friction, time):
    ball.Vel.x = 0
    ySpin = 2 / ball.radius
    ball.spinY = ySpin

    friction_force_x = spin.SpinY(ball, friction, time)
    msg = ""
    if friction_force_x <= 0:
        msg += "x friction force should be positive ball is skidding left, "
    if ball.spinY >= ySpin:
        msg += "y spin should have decreased ball is skidding left, "
    if msg == "": return "x skidding left test passed"
    return msg


def test_roll_up(ball, friction, time):
    ball.Vel.y = 2
    xSpin = -ball.Vel.y / ball.radius
    ball.spinX = xSpin

    friction_force_y = spin.SpinX(ball, friction, time)
    msg = ""
    if friction_force_y != 0:
        msg += "y friction force should be 0 ball is rolling up, "
    if ball.spinX != xSpin:
        msg += "x spin should not have changed ball is rolling up, "
    if msg == "": return "y rolling up test passed"
    return msg

def test_slide_up(ball, friction, time):
    ball.Vel.y = 2
    xSpin = 0
    ball.spinX = xSpin

    friction_force_y = spin.SpinX(ball, friction, time)
    msg = ""
    if friction_force_y >= 0:
        msg += "y friction force should be negative, ball is sliding up, "
    if ball.spinX >= xSpin:
        msg += "x spin should decrease, ball is sliding up, "
    if msg == "": return "y sliding up test passed"
    return msg

def test_skid_up(ball, friction, time):
    ball.Vel.y = 0
    xSpin = 2 / ball.radius
    ball.spinX = xSpin

    friction_force_y = spin.SpinX(ball, friction, time)
    msg = ""
    if friction_force_y >= 0:
        msg += "y friction force should be negative, ball is skidding up, "
    if ball.spinX >= xSpin:
        msg += "x spin should decrease, ball is skidding up, "
    if msg == "": return "y skidding up test passed"
    return msg

def test_roll_down(ball, friction, time):
    ball.Vel.y = -2
    xSpin = -ball.Vel.y / ball.radius
    ball.spinX = xSpin

    friction_force_y = spin.SpinX(ball, friction, time)
    msg = ""
    if friction_force_y != 0:
        msg += "y friction force should be 0, ball is rolling down, "
    if ball.spinX != xSpin:
        msg += "x spin should not have changed, ball is rolling down, "
    if msg == "": return "y rolling down test passed"
    return msg

def test_slide_down(ball, friction, time):
    ball.Vel.y = -2
    xSpin = 0
    ball.spinX = xSpin

    friction_force_y = spin.SpinX(ball, friction, time)
    msg = ""
    if friction_force_y <= 0:
        msg += "y friction force should be positive, ball is sliding down, "
    if ball.spinX <= xSpin:
        msg += "x spin should have increased, ball is sliding down, "
    if msg == "": return "y sliding down test passed"
    return msg

def test_skid_down(ball, friction, time):
    ball.Vel.y = 0
    xSpin = -2 / ball.radius
    ball.spinX = xSpin

    friction_force_y = spin.SpinX(ball, friction, time)
    msg = ""
    if friction_force_y <= 0:
        msg +="y friction force should be positive, ball is skidding down, "
    if ball.spinX <= xSpin:
        msg += "x spin should have increased, ball is skidding down, "
    if msg == "": return "y skidding down test passed"
    return msg


if __name__ == "__main__":
    Test()