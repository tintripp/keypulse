import pygame

from .state import State

class PlayState(State):
    def __init__(self, persistent_data = None):
        super().__init__(persistent_data)

    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.done = True

    def update(self, dt): 
        print(dt)

    def draw(self, screen): 
        pass