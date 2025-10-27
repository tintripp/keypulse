import pygame

FRAMERATE = 60

class Game:
    def __init__(self):
        self.done = False
        self.window = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self, dt):
        print(dt)

    def draw(self):
        pass

    def begin(self):
        while not self.done:
            dt = self.clock.tick(FRAMERATE)

            self.handle_events()
            self.update(dt)
            self.draw()

            pygame.display.update()

Game().begin()