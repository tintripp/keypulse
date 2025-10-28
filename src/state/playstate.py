import pygame

from .state import State
from src.chart import Chart

class PlayState(State):
    def __init__(self, persistent_data = None):
        super().__init__(persistent_data)

        #SETUP STATE

        #LOAD CHART INTO A LIST OF NOTE OBJECTS.
        notes = Chart.load("tutorial") #load song name from persistent data

        Chart.print(notes)

    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.done = True

    def update(self, dt): 
        print(dt)

    def draw(self, screen): 
        pass