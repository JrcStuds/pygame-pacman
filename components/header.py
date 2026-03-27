import pygame
from src.settings import *


"""
text_spritesheet = {
    "c": (2*8, 0*8),
    "e": (5*8, 0*8),
    "g": (6*8, 0*8),
    "h": (7*8, 0*8),
    "i": (8*8, 0*8),
    "o": (14*8, 0*8),
    "r": (2*8, 1*8),
    "s": (3*8, 1*8),
    "0": (0*8, 2*8),
    "1": (1*8, 2*8),
    "2": (2*8, 2*8),
    "3": (3*8, 2*8),
    "4": (4*8, 2*8),
    "5": (5*8, 2*8),
    "6": (6*8, 2*8),
    "7": (7*8, 2*8),
    "8": (8*8, 2*8),
    "9": (9*8, 2*8),
}
"""


class Header:
    def __init__(self, tileset):
        self.score = 0
        self.tileset = {
            "c": tileset.subsurface(pygame.Rect(2*TILE_SIZE, 0*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "e": tileset.subsurface(pygame.Rect(4*TILE_SIZE, 0*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "g": tileset.subsurface(pygame.Rect(6*TILE_SIZE, 0*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "h": tileset.subsurface(pygame.Rect(7*TILE_SIZE, 0*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "i": tileset.subsurface(pygame.Rect(8*TILE_SIZE, 0*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "o": tileset.subsurface(pygame.Rect(14*TILE_SIZE, 0*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "r": tileset.subsurface(pygame.Rect(2*TILE_SIZE, 1*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "s": tileset.subsurface(pygame.Rect(3*TILE_SIZE, 1*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "0": tileset.subsurface(pygame.Rect(0*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "1": tileset.subsurface(pygame.Rect(1*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "2": tileset.subsurface(pygame.Rect(2*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "3": tileset.subsurface(pygame.Rect(3*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "4": tileset.subsurface(pygame.Rect(4*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "5": tileset.subsurface(pygame.Rect(5*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "6": tileset.subsurface(pygame.Rect(6*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "7": tileset.subsurface(pygame.Rect(7*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "8": tileset.subsurface(pygame.Rect(8*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
            "9": tileset.subsurface(pygame.Rect(9*TILE_SIZE, 2*TILE_SIZE, TILE_SIZE, TILE_SIZE)),
        }
    

    def draw(self):
        blits = []
        
        for i, letter in enumerate("highscore"):
            blits.append((self.tileset[letter], (i*TILE_SIZE, 0*TILE_SIZE)))

        for i, digit in enumerate(str(self.score)):
            blits.append((self.tileset[digit], ((6 - len(str(self.score)) + i)*TILE_SIZE, 1*TILE_SIZE)))

        return blits
