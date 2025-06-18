from rogue_engine.game import Game
import pyglet

game = Game(60, 30)

window = pyglet.window.Window(game.map_width * game.tile_size, game.map_height * game.tile_size, "PyRogue")
# game.start_gameloop()

game.player.init_sprite()

@window.event
def on_draw():
    window.clear()
    game.player.draw(window.height)
    game.map.draw(window.height)

        
pyglet.app.run()


