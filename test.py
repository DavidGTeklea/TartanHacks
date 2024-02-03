from data import GameActionData
from minecraft_controller import MinecraftController


dig_test = [0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 0, 0, 0, 0]
hit_test = [0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100]

mc_controller = MinecraftController()

for num in dig_test:
    data = GameActionData(bicep_flex=num, lean_forward=0)
    mc_controller.game_actions(data)