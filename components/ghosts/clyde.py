import pygame, math, random
from src.settings import *
from ..ghost import Ghost



class Clyde(Ghost):
    def __init__(self, tileset):
        super().__init__()

        self.name = "clyde"
        
        self.sprites["up"] = tileset.subsurface(TILESET[f"{self.name}-up"])
        self.sprites["down"] = tileset.subsurface(TILESET[f"{self.name}-down"])
        self.sprites["left"] = tileset.subsurface(TILESET[f"{self.name}-left"])
        self.sprites["right"] = tileset.subsurface(TILESET[f"{self.name}-right"])

        self.pos = pygame.Vector2((TILE_HORIZONTAL - 2) * TILE_SIZE, (GAME_TILE_VERTICAL - 2) * TILE_SIZE)
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