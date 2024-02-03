from data import GameActionData
from minecraft_controller import MinecraftController
import time 

time.sleep(3)
dig_test = [0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 0, 0, 0, 0]
hit_test = [0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100]

mc_controller = MinecraftController()

for num in dig_test:
    data = GameActionData(flex_value=num, jump_value=0)
    time.sleep(0.5)
    mc_controller.game_actions(data)