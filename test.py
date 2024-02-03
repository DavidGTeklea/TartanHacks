from data import GameActionData, RotationData
from minecraft_controller import MinecraftController

import time 

time.sleep(3)
dig_test = [0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 0, 0, 0, 0]
hit_test = [0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100]


turn_test = [0, 81, 0, 10, 0, 0, 90, 2, 0, 0.9, 0, 90, 90, 0]

mc_controller = MinecraftController()

for num in turn_test:
    data = RotationData(y_angle=num, x_angle=0)
    time.sleep(0.5)
    mc_controller.rotate_camera(data)
    data = RotationData(y_angle=0, x_angle=num)
    time.sleep(0.5)
    mc_controller.rotate_camera(data)

for num in dig_test:
    data = GameActionData(flex_value=num, jump_value=0)
    time.sleep(0.5)
    mc_controller.game_actions(data)
