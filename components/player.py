import pygame
from src.settings import *


class Player():
    def __init__(self, game):
        self.game = game

        self.tileset = pygame.image.load('./assets/sprites.png').convert()
        self.tileset.set_colorkey((0, 0, 0))

        self.sprites = self.init_sprites()
        self.surface = self.sprites["closed"]

        self.width, self.height = 8, 8
        self.surface_width, self.surface_height = 16, 16
        
        self.pos = pygame.Vector2(8, 8)
        self.dir = pygame.Vector2(0, 1)
        self.next_dir = pygame.Vector2(0, 1)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)

        self.last_tile = None

        self.sprite_dir = "left"
        self.framecount = 0
        self.mouth_state = "closed"
    


    def draw(self):
        blits = [(self.surface, (self.pos.x - self.width / 2, self.pos.y - self.width / 2, self.surface_width, self.surface_height)),]
        return blits
    


    def update(self, controls, collrects, dt):
        if controls["up"]: self.dir.y = -1
        elif controls["down"]: self.dir.y = 1
        elif controls["left"]: self.dir.x = -1
        elif controls["right"]: self.dir.x = 1

        self.pos.x += PLAYER_SPEED * self.dir.x * self.game.dt

        collision = self.check_collision(collrects)

        if collision and self.dir.x:
            self.pos.x = collision[0] - (self.rect.width * self.dir.x)
            self.dir.x = 0
            

        self.pos.y += PLAYER_SPEED * self.dir.y * dt
        collision = self.check_collision(collrects)
        
        if collision and self.dir.y:
            self.pos.y = collision[1] - (self.rect.height * self.dir.y)
            self.dir.y = 0


        if self.pos.x <= -self.rect.width - 1:
            self.pos.x = GAME_SIZE[0]
            self.pos.y = 14*TILE_SIZE
        if self.pos.x >= GAME_SIZE[0] + 1:
            self.pos.x = -self.rect.width
            self.pos.y = 14*TILE_SIZE


        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        

        if self.dir.x > 0:
            self.sprite_dir = "right"
        if self.dir.x < 0:
            self.sprite_dir = "left"
        if self.dir.y > 0:
            self.sprite_dir = "down"
        if self.dir.y < 0:
            self.sprite_dir = "up"


        self.framecount += 1
        if self.framecount >= 8:
            match self.mouth_state:
                case "closed": self.mouth_state = "1"
                case "1": self.mouth_state = "2"
                case "2": self.mouth_state = "closed"
            self.framecount = 0

        if self.mouth_state == "closed":
            self.surface = self.sprites["closed"]
        else:
            self.surface = self.sprites[f"{self.sprite_dir}-{self.mouth_state}"]

        


    
    def init_sprites(self):
        sprites = {}
        name = "pacman"
        for sprite in TILESET_SPRITES.keys():
            if sprite[:len(name)] == name:
                sprites[sprite[ len(name) + 1:]] = self.tileset.subsurface(TILESET_SPRITES[sprite])
        return sprites



    def check_collision(self, rects):
        player_sides = {
            "top": self.pos.y,
            "bottom": self.pos.y + self.rect.height - 1,
            "left": self.pos.x,
            "right": self.pos.x + self.rect.width - 1,
        }
        for rect in rects:
            rect_sides = {
                "top": rect[1],
                "bottom": rect[1] + rect[3] - 1,
                "left": rect[0],
                "right": rect[0] + rect[2] - 1,
            }
            if (
                ((rect_sides["top"] <= player_sides["top"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["left"] <= rect_sides["right"])) or
                ((rect_sides["top"] <= player_sides["top"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["right"] <= rect_sides["right"])) or
                ((rect_sides["top"] <= player_sides["bottom"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["left"] <= rect_sides["right"])) or
                ((rect_sides["top"] <= player_sides["bottom"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["right"] <= rect_sides["right"]))
            ):
                return rect
        return None