import pygame
from src.settings import *
from .world import World
from .player import Player
from .ghosts.blinky import Blinky
from .ghosts.pinky import Pinky
from .ghosts.inky import Inky
from .ghosts.clyde import Clyde



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        pygame.joystick.init()
        self.joystick = None

        self.keys = {"up": False, "down": False, "left": False, "right": False}

        self.tileset = pygame.image.load('./assets/tileset.png').convert()
        self.tileset.set_colorkey((0,0,0))

        self.world = World(self.tileset)
        self.player = Player(self.tileset)
        self.ghosts = [Blinky(self.tileset), Pinky(self.tileset), Inky(self.tileset), Clyde(self.tileset)]
        print(self.ghosts[0].name, self.ghosts[0].pos)


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

            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >= 0.5: self.keys["right"], self.keys["left"] = True, False
                    elif event.value <= -0.5: self.keys["right"], self.keys["left"] = False, True
                    else: self.keys["right"], self.keys["left"] = False, False
                if event.axis == 1:
                    if event.value >= 0.5: self.keys["down"], self.keys["up"] = True, False
                    elif event.value <= -0.5: self.keys["down"], self.keys["up"] = False, True
                    else: self.keys["down"], self.keys["up"] = False, False

            if event.type == pygame.JOYDEVICEADDED:
                self.joystick = pygame.joystick.Joystick(0)
            if event.type == pygame.JOYDEVICEREMOVED:
                self.joystick = None

            
    

    def update(self):
        world_rects = self.world.get_rects()
        wall_rects = world_rects["wall"]
        pellet_rects = world_rects["pellet"]
        self.player.update(self.keys, wall_rects, self.dt)
        pellet_collision = self.player.check_pellet_collision(pellet_rects)
        self.world.pellet_collision(pellet_collision)
        for ghost in self.ghosts:
            ghost.update(self.world.map, wall_rects, self.dt)
            ghost.set_target(self.player.pos, self.player.dir, self.ghosts[0].pos)


    def draw(self):
        self.screen.fill("black")
        fblits = []
        fblits.extend(self.world.draw())
        fblits.extend(self.player.draw())
        for ghost in self.ghosts:
            fblits.extend(ghost.draw())
        self.screen.fblits(fblits)
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60) / 1000
        
        pygame.joystick.quit()
        pygame.quit()