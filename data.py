class GameActionData:
    flex_value: int
    jump_value: int
    forward_value: int
    backward_value: int
    left_value: int
    right_value: int
    tiltup_value: int
    tiltdown_value: int
    tiltleft_value: int
    tiltright_value: int

    def __init__(self, flex_value, jump_value, forward_value, backward_value, left_value, right_value, tiltup_value, tiltdown_value, tiltleft_value, tiltright_value):
        self.flex_value = flex_value
        self.jump_value = jump_value
        self.forward_value = forward_value
        self.backward_value = backward_value
        self.left_value = left_value
        self.right_value = right_value
        self.tiltup_value = tiltup_value
        self.tiltdown_value = tiltdown_value
        self.tiltleft_value = tiltleft_value
        self.tiltright_value = tiltright_value