class Player:
    def __init__(self, model: str, hp: int, mobility: int, base_strength: int, base_health: int, base_dodge: int):
        self.model = model
        self.mobility = mobility
        self.strength, self.hp, self.dodge = base_strength, base_health, base_dodge
        self.x, self.y = 0, 0