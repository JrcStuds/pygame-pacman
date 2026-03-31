import pygame, math, random
from src.settings import *
from ..ghost import Ghost



class Clyde(Ghost):
    def __init__(self, tileset):
        super().__init__()

        self.name = "clyde"
        
        for sprite in TILESET_SPRITES.keys():
            if sprite[0] == "g":
                self.sprites[sprite[6:]] = tileset.subsurface(TILESET_SPRITES[sprite])
            if sprite[0] == self.name[0]:
                self.sprites[sprite[(len(self.name) + 1):]] = tileset.subsurface(TILESET_SPRITES[sprite])

        self.pos = pygame.Vector2(14*TILE_SIZE, 11*TILE_SIZE)
        self.dir = pygame.Vector2(0, -1)
        self.target = pygame.Vector2(0, 0)



    def set_target(self, player_pos, player_dir, blinky_pos):
        if (
            abs(self.pos.x // TILE_SIZE - self.target.x) < 4 and
            abs(self.pos.y // TILE_SIZE - self.target.y) < 4
        ):
            self.target.x = random.randint(0, TILE_HORIZONTAL)
            self.target.y = random.randint(0, GAME_TILE_VERTICAL)
        return