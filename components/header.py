import pygame
from src.settings import *


class Header:
    def __init__(self, tileset):
        self.score = 0
        self.tileset = {}
        for char in TILESET_TEXT.keys():
            self.tileset[char] = tileset.subsurface(TILESET_TEXT[char])
    

    def draw(self):
        blits = []
        
        for i, letter in enumerate("highscore"):
            blits.append((self.tileset[letter], ((i + 10)*TILE_SIZE, 0*TILE_SIZE)))

        for i, digit in enumerate(str(self.score)):
            blits.append((self.tileset[digit], ((7 - len(str(self.score)) + i)*TILE_SIZE, 1*TILE_SIZE)))

        return blits
