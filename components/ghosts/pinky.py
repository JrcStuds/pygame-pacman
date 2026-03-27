import pygame, math, random
from src.settings import *
from ..ghost import Ghost



class Pinky(Ghost):
    def __init__(self, tileset):
        super().__init__()

        self.name = "pinky"
        
        self.sprites["up"] = tileset.subsurface(TILESET[f"{self.name}-up"])
        self.sprites["down"] = tileset.subsurface(TILESET[f"{self.name}-down"])
        self.sprites["left"] = tileset.subsurface(TILESET[f"{self.name}-left"])
        self.sprites["right"] = tileset.subsurface(TILESET[f"{self.name}-right"])

        self.pos = pygame.Vector2((TILE_HORIZONTAL - 2) * TILE_SIZE, (TILE_VERTICAL - 2) * TILE_SIZE)
        self.dir = pygame.Vector2(0, -1)
        self.target = pygame.Vector2(0, 0)



    def set_target(self, player_pos, player_dir, blinky_pos):
        self.target.x = math.floor(player_pos.x // TILE_SIZE) + player_dir.x * 4
        self.target.y = math.floor(player_pos.y // TILE_SIZE) + player_dir.y * 4
        return