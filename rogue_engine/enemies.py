import pyglet
from rogue_engine.camera import Camera
from pyglet.gl import (
    GL_NEAREST,
    glTexParameteri,
    GL_TEXTURE_2D,
    GL_TEXTURE_MIN_FILTER,
    GL_TEXTURE_MAG_FILTER
    )
class Enemy:
    def __init__(self, model: str, hp: int, mobility: int, base_strength: int, base_dodge: int, sprite_path: str):
        self.model = model
        self.mobility = mobility
        self.strength, self.hp, self.dodge = base_strength, hp, base_dodge
        self.x, self.y = 0, 0
        self.sprite_path = sprite_path;

    def draw(self, window_height, tile_size, camera: Camera):
        if self.sprite:
            if camera.x + camera.x_offset > self.x > camera.x and camera.y + camera.y_offset > self.y > camera.y: 
                screen_x = int((self.x - camera.x) * tile_size * self.sprite.scale)
                screen_y = int(window_height - ((self.y - camera.y + 1) * tile_size * self.sprite.scale))

                self.sprite.x = screen_x
                self.sprite.y = screen_y
                self.sprite.anchor_x = 0
                self.sprite.anchor_y = 0
                self.sprite.draw()
    
    def init_sprite(self):
        image = pyglet.image.load(self.sprite_path)
        
        texture = image.get_texture()
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        self.sprite = pyglet.sprite.Sprite(texture, self.x, self.y)
        self.sprite.anchor_x = 0
        self.sprite.anchor_y = 0
        self.sprite.scale = 2



Ennemy_Types = [
    {"model": "\033[32mG\033[0m", "sprite": "src/sprites/goblin.png", "range_hp": (1, 5), "range_dodge": (2, 10), "range_strength": (1,4), "mobility": 2}
]