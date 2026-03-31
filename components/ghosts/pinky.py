import pygame, math, random
from src.settings import *
from ..ghost import Ghost



class Pinky(Ghost):
    def __init__(self, tileset):
        super().__init__()

        self.name = "pinky"
        
        for sprite in TILESET_SPRITES.keys():
            if sprite[0] == "g":
                self.sprites[sprite[6:]] = tileset.subsurface(TILESET_SPRITES[sprite])
            if sprite[0] == self.name[0]:
                self.sprites[sprite[(len(self.name) + 1):]] = tileset.subsurface(TILESET_SPRITES[sprite])

        self.pos = pygame.Vector2(12*TILE_SIZE, 11*TILE_SIZE)
        self.dir = pygame.Vector2(0, -1)
        self.target = pygame.Vector2(0, 0)



    def set_target(self, player_pos, player_dir, blinky_pos):
        self.target.x = math.floor(player_pos.x // TILE_SIZE) + player_dir.x * 4
        self.target.y = math.floor(player_pos.y // TILE_SIZE) + player_dir.y * 4
        return