import pygame

from .state import State
from state.playstate import PlayState

class TitleState(State):
    def __init__(self):
        super().__init__()

    def start(self, persistent_data): 
        super().start(persistent_data)

    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print('hey johnny')
            if event.key == pygame.K_SPACE:
                self.done = True
                self.next_state = PlayState()

    def update(self, dt): 
        pass

    def draw(self, screen): 
        pass