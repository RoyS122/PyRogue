from rogue_engine.map import GameMap
from rogue_engine.player import Player
import os
import msvcrt
import random



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

class game:
    def __init__(self, map_width: int, map_height: int):
        self.map = GameMap(map_width, map_height)
        self.map.generate_rooms(random.randint(3, 7))
        self.player = Player("@", 10, 1, 1, 1, 1)
        r = random.choice(self.map.rooms)
        self.player.x, self.player.y = r.x + r.width - (r.width // 2), r.y + r.height - (r.height // 2)
    
    def start_gameloop(self):
        while(True): 
            cls()
            self.display()
            print("Press a key (q to quit): ", end='', flush=True)
            key = msvcrt.getch()
            print(key)# Echo the key
            if key == b'q':
                print("Exiting game loop.")
                break
            move = {"x": 0, "y": 0}
            if key == b'H':
                if self.player.y > 0:
                    move["y"] -= 1;
            if key == b'P':
                if self.player.y < len(self.map.array) - 1:
                    move["y"] += 1;
            if key == b'M':
                if self.player.x < len(self.map.array[0]) - 1:
                    move["x"] += 1;
            if key == b'K':
                if self.player.x > 0:
                    move["x"] -= 1;
            
            if(self.map.array[self.player.y][self.player.x + move["x"]] != "#"):
                self.player.x += move["x"]
            
            if(self.map.array[self.player.y + move["y"]][self.player.x] != "#"):
                self.player.y += move["y"]
            
            # Process the input or update the game state here
            # print(f"You entered: {user_input}")
    
    def display(self):
        rendered_lines = [];
        buffer = []
        for y in range(len(self.map.array)):
            line = list(self.map.array[y])
            buffer.append(line)

        if (self.player.x >= 0 and self.player.x < len(buffer[0])) and (self.player.y >= 0 and self.player.y < len(buffer)):
            buffer[self.player.y][self.player.x] = self.player.model
        
        for line in buffer:
            rendered_lines.append("".join(line))  
        print("\n".join(rendered_lines))
