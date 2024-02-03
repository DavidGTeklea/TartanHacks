from data import Data
from minecraft_controller import MinecraftController
import time 

time.sleep(3)
dig_test = [0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 0, 0, 0, 0]
hit_test = [0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100]

mc_controller = MinecraftController()

for num in hit_test:
    data = Data(bicep_flex=num, lean_forward=0)
    time.sleep(0.5)
    mc_controller.game_actions(data)