class GameActionData:
    flex_value: int
    jump_value: int

    def __init__(self, flex_value, jump_value):
        self.flex_value = flex_value
        self.jump_value = jump_value

class RotationData:
    x_value: int
    y_value: int

    def __init__(self, y_value, x_value):
        self.x_value = y_value
        self.y_value = x_value