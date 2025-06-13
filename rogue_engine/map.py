import random

class Room:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.doors = []

    def intersects(self, other):
        return (self.x - 1< other.x + other.width + 1 and
                self.x + self.width + 1 > other.x - 1 and
                self.y - 1< other.y + other.height + 1 and
                self.y + self.height + 1 > other.y - 1)

class GameMap:
    def __init__(self, width: int, height: int): 
        self.width = width
        self.height = height
        self.array = [[" " for j in range(width)] for i in range(height)]
        self.rooms = []

    def display(self):
        for line in self.array:
            print("".join(line))

    def add_room(self, room: Room):
        for x in range(room.width):
            for y in range(room.height):
                if x == 0 or x == room.width - 1 or y == 0 or y == room.height - 1:
                    self.array[room.y + y][room.x + x] = "#"
                else:
                    self.array[room.y + y][room.x + x] = "."

    def create_tunnel(self, x1, y1, x2, y2):
        if random.choice([True, False]):
            self.create_h_tunnel(x1, x2, y1)
            self.create_v_tunnel(y1, y2, x2)
            self.array[y2][x2] = "."
        else:
            self.create_v_tunnel(y1, y2, x1)
            self.create_h_tunnel(x1, x2, y2)
            self.array[y2][x2] = "."

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
                self.array[y][x] = "."
                if len(self.array) > y + 1 and self.array[y + 1][x] != ".":
                    self.array[y + 1][x] = "#"
                if y - 1 >= 0 and self.array[y - 1][x] != ".":
                    self.array[y - 1][x] = "#"
                

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
                self.array[y][x] = "."
                if len(self.array[0]) > x + 1 and self.array[y ][x + 1] != ".":
                    self.array[y][x + 1] = "#"
                if x - 1 >= 0 and self.array[y][x - 1] != ".":
                    self.array[y][x - 1] = "#"

    def generate_rooms(self, num_rooms):
        for _ in range(num_rooms):
            while True:
                width = random.randint(6, 16)
                height = random.randint(6, 16)
                x = random.randint(0, self.width - width - 1)
                y = random.randint(0, self.height - height - 1)
                new_room = Room(x, y, width, height)
                if all(not new_room.intersects(other) for other in self.rooms):
                    self.add_room(new_room)
                    if self.rooms:
                        prev_room = self.rooms[-1]
                        self.create_tunnel(prev_room.x + prev_room.width // 2,
                                           prev_room.y + prev_room.height // 2,
                                           new_room.x + new_room.width // 2,
                                           new_room.y + new_room.height // 2)
                    self.rooms.append(new_room)
                    break

