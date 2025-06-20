from rogue_engine.game import Game
from rogue_engine.camera import Camera

import pyglet
import ctypes

from pyglet.window import key

from pyglet.gl import (
    GL_NEAREST,
    glTexParameteri,
    GL_TEXTURE_2D,
    GL_TEXTURE_MIN_FILTER,
    GL_TEXTURE_MAG_FILTER
    )


# === Initialisation du jeu ===
game = Game(60, 30)

window = pyglet.window.Window(1200, 720, "PyRogue")

game.player.init_sprite()
for e in game.enemies:
    e.init_sprite()
cam = Camera(game.player.x, 20, game.player.y, 20)

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)



@window.event
def on_draw():
    window.clear()
    game.map.draw(window.height, cam)
    for e in game.enemies:
        e.draw(window_height=window.height, tile_size=game.tile_size, camera=cam)
    game.player.draw(window.height, tile_size=game.tile_size, camera=cam)
 

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        print("Touche Échap pressée")

@window.event
def on_key_release(symbol, modifiers):
    game.on_key_release(symbol)
    cam.x = game.player.x - cam.x_offset // 2
    cam.y = game.player.y - cam.y_offset // 2
   


pyglet.app.run()
