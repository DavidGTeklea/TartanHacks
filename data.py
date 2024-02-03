class GameActionData:
    flex_value: int
    jump_value: int
    y_move: int
    x_move: int
    y_tilt: int
    x_tilt: int

    def __init__(self, flex_value, jump_value, y_move, x_move, y_tilt, x_tilt):
        self.flex_value = flex_value
        self.jump_value = jump_value
        self.y_move = y_move
        self.x_move = x_move
        self.y_tilt = y_tilt
        self.x_tilt = x_tilt
