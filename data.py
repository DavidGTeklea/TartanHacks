class GameActionData:
    flex_value: int
    jump_value: int

    def __init__(self, flex_value, jump_value):
        self.flex_value = flex_value
        self.jump_value = jump_value

class RotationData:
    y_angle: int
    x_angle: int

    def __init__(self, y_angle, x_angle):
        self.y_angle = y_angle
        self.x_angle = x_angle