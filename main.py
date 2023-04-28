import pyxel

from player import Player
from objects import Objects
from event import Event
from input import Check_key
game_witht = 320
game_height = 160

pyxel.init(game_witht, game_height, 'Leo Broklin', 30)

tile_map_player = pyxel.image(0)
tile_map_player.load(0, 0, "tile_player.png")
tile_map_objects = pyxel.image(1)
tile_map_objects.load(0, 0, "tile_objects.png")
camera = pyxel.camera
objects = Objects(pyxel, tile_map_objects, game_witht, game_height,)
player = Player(pyxel, tile_map_player, game_witht, game_height, objects, camera)
event = Event(pyxel, player)
check_key = Check_key(pyxel, event, player)
print(list(pyxel.colors))

def update():
    check_key.check_key_pressed()
    objects.update(player)


def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    objects.draw()
    player.draw()

if __name__ == "__main__":
    pyxel.run(update, draw)
