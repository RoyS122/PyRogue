import pyglet

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

    def draw(self, window_height):
        if self.sprite:
            self.sprite.x = self.x
            self.sprite.y = window_height - self.y - self.sprite.height
            self.sprite.draw()

