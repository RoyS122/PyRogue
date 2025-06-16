class Enemy:
    def __init__(self, model: str, hp: int, mobility: int, base_strength: int, base_dodge: int):
        self.model = model
        self.mobility = mobility
        self.strength, self.hp, self.dodge = base_strength, hp, base_dodge
        self.x, self.y = 0, 0


Ennemy_Types = [
    {"model": "\033[32mG\033[0m", "range_hp": (1, 5), "range_dodge": (2, 10), "range_strength": (1,4), "mobility": 2}
]