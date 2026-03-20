import pygame
from src.settings import *
from .ghost import Ghost



class Inky(Ghost):
    def __init__(self, tileset):
        super().__init__()
        
        self.sprites["up"] = tileset.subsurface(TILESET["inky-up"])
        self.sprites["down"] = tileset.subsurface(TILESET["inky-down"])
        self.sprites["left"] = tileset.subsurface(TILESET["inky-left"])
        self.sprites["right"] = tileset.subsurface(TILESET["inky-right"])

        self.pos = pygame.Vector2((TILE_HORIZONTAL - 2) * TILE_SIZE, (TILE_VERTICAL - 2) * TILE_SIZE)
        self.dir = pygame.Vector2(0, -1)
        self.target = pygame.Vector2(0, 0)