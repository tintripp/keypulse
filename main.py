import pygame

FRAMERATE = 60
SCREEN_WIDTH = (1280,720)

class Game:
    def __init__(self, start_state):
        self.done = False
        self.window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.screen = pygame.Surface(SCREEN_WIDTH)

        self.states = [start_state]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            self.states[-1].handle_event(event)

    def update(self, dt):
        #update ONLY the LAST state
        self.states[-1].update(dt)

        if (self.states[-1].done):
            if (self.states[-1].next_state):
                next_state = self.states[-1].next_state
                self.states.pop()
                self.states.append(next_state)
            else:
                self.done = True

    def draw(self):
        self.screen.fill((127,)*3)

        #draw all states
        for state in self.states:
            state.draw(self.screen)

        #blit screen onto window
        self.window.blit(self.screen)

    def begin(self):
        while not self.done:
            dt = self.clock.tick(FRAMERATE)

            self.handle_events()
            self.update(dt)
            self.draw()

            pygame.display.flip()

from state.titlestate import TitleState
Game(TitleState()).begin()