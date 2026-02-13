import pygame
from src.settings import *
from .world import World


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        self.world = World()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    

    def update(self):
        pass


    def draw(self):
        fblits = []
        fblits.extend(self.world.draw())
        self.screen.fblits(fblits)
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60) / 1000
        
        pygame.quit()