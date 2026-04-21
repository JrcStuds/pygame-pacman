import pygame
from src.settings import *
from .world import World
from .player import Player
from .header import Header
from components.ghosts.ghost import Ghost



class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(DISPLAY_SIZE, pygame.SCALED | pygame.RESIZABLE)
        self.game_screen = pygame.Surface(GAME_SIZE)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True

        pygame.joystick.init()
        self.joystick = None

        self.keys = {
            "up": [pygame.K_UP, pygame.K_w],
            "down": [pygame.K_DOWN, pygame.K_s],
            "left": [pygame.K_LEFT, pygame.K_a],
            "right": [pygame.K_RIGHT, pygame.K_d],
        }
        self.controls = {"up": False, "down": False, "left": False, "right": False}

        self.tileset = pygame.image.load('./assets/sprites.png').convert()
        self.tileset.set_colorkey((0,0,0))
        self.player = Player(self)
        self.ghosts = [
            Ghost("blinky", game=self),
            Ghost("pinky", game=self),
            Ghost("inky", game=self),
            Ghost("clyde", game=self),
        ]
        self.ghost_state_timer = [0, "chase"]

        self.map_sprite = pygame.image.load('./assets/map.png').convert()
        self.world = World(self.map_sprite)

        self.text_tileset = pygame.image.load('./assets/text.png').convert()
        self.header = Header(self.text_tileset)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                for key in self.keys.keys():
                    if event.key in self.keys[key]:
                        self.controls[key] = True

            if event.type == pygame.KEYUP:
                for key in self.keys.keys():
                    if event.key in self.keys[key]:
                        self.controls[key] = False

            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value >= 0.5: self.controls["right"], self.controls["left"] = True, False
                    elif event.value <= -0.5: self.controls["right"], self.controls["left"] = False, True
                    else: self.controls["right"], self.controls["left"] = False, False
                if event.axis == 1:
                    if event.value >= 0.5: self.controls["down"], self.controls["up"] = True, False
                    elif event.value <= -0.5: self.controls["down"], self.controls["up"] = False, True
                    else: self.controls["down"], self.controls["up"] = False, False

            if event.type == pygame.JOYDEVICEADDED:
                self.joystick = pygame.joystick.Joystick(0)
            if event.type == pygame.JOYDEVICEREMOVED:
                self.joystick = None

            
    

    def update(self):
        world_rects = self.world.get_rects()
        wall_rects = world_rects["wall"]
        pellet_rects = world_rects["pellet"]
        self.player.update(self.controls, wall_rects, self.dt)
        pellet_collision = self.player.check_collision(pellet_rects)
        if pellet_collision:
            self.world.pellet_collision(pellet_collision)
            self.header.score += PELLET_SCORE
        for ghost in self.ghosts:
            ghost.update()
            if self.player.check_collision([ghost.rect]):
                print(f"{ghost.name} killed pacman")

        self.ghost_state_timer[0] += 1
        if self.ghost_state_timer[0] >= 20*60 and self.ghost_state_timer[1] == "chase":
            self.ghost_state_timer = [0, "scatter"]
        if self.ghost_state_timer[0] >= 7*60 and self.ghost_state_timer[1] == "scatter":
            self.ghost_state_timer = [0, "chase"]


    def draw(self):
        self.display.fill("black")
        self.game_screen.fill("black")

        fblits = [] # for game_screen
        fblits.extend(self.world.draw())
        fblits.extend(self.player.draw())
        for ghost in self.ghosts:
            fblits.extend(ghost.draw())
        self.game_screen.fblits(fblits)

        fblits = []
        fblits.append((self.game_screen, (0, 3*TILE_SIZE)))
        fblits.extend(self.header.draw())
        self.display.fblits(fblits)

        pygame.display.flip()


    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.dt = self.clock.tick(60) / 1000
        
        pygame.joystick.quit()
        pygame.quit()