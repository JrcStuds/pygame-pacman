import pygame
from src.settings import *
from .world import World
from .player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        self.keys = {"up": False, "down": False, "left": False, "right": False}

        self.world = World()
        self.player = Player()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP: self.keys["up"] = True
                    case pygame.K_DOWN: self.keys["down"] = True
                    case pygame.K_LEFT: self.keys["left"] = True
                    case pygame.K_RIGHT: self.keys["right"] = True

            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_UP: self.keys["up"] = False
                    case pygame.K_DOWN: self.keys["down"] = False
                    case pygame.K_LEFT: self.keys["left"] = False
                    case pygame.K_RIGHT: self.keys["right"] = False
            
    

    def update(self):
        world_rects = self.world.get_rects()
        wall_rects = world_rects["wall"]
        pellet_rects = world_rects["pellet"]
        self.player.update(self.keys, wall_rects, self.dt)
        pellet_collision = self.player.check_pellet_collision(pellet_rects)
        self.world.pellet_collision(pellet_collision)


    def draw(self):
        fblits = []
        fblits.extend(self.world.draw())
        fblits.append(self.player.draw())
        self.screen.fblits(fblits)
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60) / 1000
        
        pygame.quit()