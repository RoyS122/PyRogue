import pyglet
from rogue_engine.camera import Camera
class Player:
    def __init__(self, model: str, sprite_path: str, hp: int, mobility: int, base_strength: int, base_health: int, base_dodge: int):
        self.sprite_path = sprite_path
        self.sprite = None  # Will be initialized later
        self.model = model
        self.mobility = mobility
        self.strength, self.hp, self.dodge = base_strength, base_health, base_dodge
        self.x, self.y = 0, 0

    def init_sprite(self):
        image = pyglet.image.load(self.sprite_path)
        self.sprite = pyglet.sprite.Sprite(image, self.x, self.y)
        self.sprite.anchor_x = 0
        self.sprite.anchor_y = 0
        self.sprite.scale = 2

  
    
    def draw(self, window_height, tile_size, camera: Camera):
        if self.sprite:
            screen_x = (self.x - camera.x) * tile_size * self.sprite.scale
            screen_y = window_height - ((self.y - camera.y + 1) * tile_size * self.sprite.scale)

            self.sprite.x = screen_x
            self.sprite.y = screen_y
            self.sprite.draw()

