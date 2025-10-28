class Note:
    def __init__(self, char, x, y, time, lifespan):
        self.char = char
        self.x = x
        self.y = y
        self.time = time
        self.lifespan = lifespan

    def update(self, dt):
        pass

    def draw(self, screen):
        pass 
        #draw 2 circles, one which has a constant size, and one which has a size of (BIG_SIZE - ELAPSED_TIME) or something like that