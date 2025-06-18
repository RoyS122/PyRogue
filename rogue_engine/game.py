from rogue_engine.map import GameMap
from rogue_engine.player import Player
from rogue_engine.enemies import Enemy, Ennemy_Types
import os
import msvcrt
import random

from typing import List




def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



class Game:
    def __init__(self, map_width: int, map_height: int):
        self.map = GameMap(map_width, map_height)
        self.map.generate_rooms(random.randint(2, 5))
      

        self.player = Player("\033[38;5;208m@\033[0m", 10, 1, 1, 2, 1)
        room = random.choice(self.map.rooms)
        self.player.x = room.x + room.width // 2
        self.player.y = room.y + room.height // 2

        self.enemies: List[Enemy] = []
        for r in self.map.rooms:
            enn_type = random.choice(Ennemy_Types)
            new_enemy = Enemy(
                enn_type["model"],
                random.randint(*enn_type["range_hp"]),
                enn_type["mobility"],
                random.randint(*enn_type["range_strength"]),
                random.randint(*enn_type["range_dodge"])
            )
            print(r.x, r.y, r.width, r.height)
            new_enemy.x, new_enemy.y = random.randint(r.x + 1, r.x + r.width - 2), random.randint(r.y + 1, r.y + r.height - 2)
            self.enemies.append(new_enemy)

        self.ennemies = []
    
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
            
            if(self.map.array[self.player.y + move["y"]][self.player.x + move["x"]] == "."):
                # print("there is the char : '" + self.map.array[self.player.y + move["y"]][self.player.x + move["x"]]+ "'", move, input())
             
                enn_check = self.checkForEnemy(self.player.x + move["x"],  self.player.y + move["y"])
                if enn_check != -1:
                    enn = self.enemies[enn_check]
                    enn.hp -= self.player.strength;
                    
                
                    if enn.hp < 0:
                        del self.enemies[enn_check]
                        enn_check = -1;
                    else: 
                        self.player.hp -= enn.strength
                if enn_check == -1:
                    self.player.x += move["x"]
                    self.player.y += move["y"]

            if self.player.hp < 0:
                quit()
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

        for e in self.enemies:
            if (e.x >= 0 and e.x < len(buffer[0])) and (e.y >= 0 and e.y < len(buffer)):
                buffer[e.y][e.x] = e.model
        
        for line in buffer:
            rendered_lines.append("".join(line))  
        print("\n".join(rendered_lines))
    
    def checkForEnemy(self, x: int, y: int)->int: 
     
       
        for i, e in enumerate(self.enemies):
          
            if e.x == x and e.y == y:
                return i
        return -1
