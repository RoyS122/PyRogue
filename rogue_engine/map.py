class GameMap:
    def __init__(self, width, height): 
        self.array = [[" " for j in range(width)] for i in range(height)]
        # print(self.array)
    
    def display(self):
        for line in self.array:
            print(line);