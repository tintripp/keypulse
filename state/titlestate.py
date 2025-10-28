import pygame

from .state import State
from state.playstate import PlayState

class TitleState(State):
    def __init__(self, persistent_data = None):
        super().__init__(persistent_data)

    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print('hey johnny')
            if event.key == pygame.K_SPACE:
                self.next_state = PlayState()
                self.done = True

    def update(self, dt): 
        pass

    def draw(self, screen): 
        pass