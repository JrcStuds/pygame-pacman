import pygame
from src.settings import *


class World:
    def __init__(self, tileset):
        self.tiles = {
            "blank": tileset.subsurface(TILESET["blank"]),
            "topleft-corner-inside": tileset.subsurface(TILESET["topleft-corner-inside"]),
            "topright-corner-inside": tileset.subsurface(TILESET["topright-corner-inside"]),
            "bottomleft-corner-inside": tileset.subsurface(TILESET["bottomleft-corner-inside"]),
            "bottomright-corner-inside": tileset.subsurface(TILESET["bottomright-corner-inside"]),
            "topleft-corner-outside": tileset.subsurface(TILESET["topleft-corner-outside"]),
            "topright-corner-outside": tileset.subsurface(TILESET["topright-corner-outside"]),
            "bottomleft-corner-outside": tileset.subsurface(TILESET["bottomleft-corner-outside"]),
            "bottomright-corner-outside": tileset.subsurface(TILESET["bottomright-corner-outside"]),
            "topleft-corner-thick": tileset.subsurface(TILESET["topleft-corner-thick"]),
            "topright-corner-thick": tileset.subsurface(TILESET["topright-corner-thick"]),
            "bottomleft-corner-thick": tileset.subsurface(TILESET["bottomleft-corner-thick"]),
            "bottomright-corner-thick": tileset.subsurface(TILESET["bottomright-corner-thick"]),
            "topleft-corner-square": tileset.subsurface(TILESET["topleft-corner-square"]),
            "topright-corner-square": tileset.subsurface(TILESET["topright-corner-square"]),
            "bottomleft-corner-square": tileset.subsurface(TILESET["bottomleft-corner-square"]),
            "bottomright-corner-square": tileset.subsurface(TILESET["bottomright-corner-square"]),
            "top-wall-thin": tileset.subsurface(TILESET["top-wall-thin"]),
            "bottom-wall-thin": tileset.subsurface(TILESET["bottom-wall-thin"]),
            "left-wall-thin": tileset.subsurface(TILESET["left-wall-thin"]),
            "right-wall-thin": tileset.subsurface(TILESET["right-wall-thin"]),
            "top-wall-thick": tileset.subsurface(TILESET["top-wall-thick"]),
            "bottom-wall-thick": tileset.subsurface(TILESET["bottom-wall-thick"]),
            "left-wall-thick": tileset.subsurface(TILESET["left-wall-thick"]),
            "right-wall-thick": tileset.subsurface(TILESET["right-wall-thick"]),
            "left-gate": tileset.subsurface(TILESET["left-gate"]),
            "right-gate": tileset.subsurface(TILESET["right-gate"]),
            "main-gate": tileset.subsurface(TILESET["main-gate"]),
            "pellet": tileset.subsurface(TILESET["pellet"]),
            "powerup": tileset.subsurface(TILESET["powerup"]),
        }
        self.map = self.init_map()
        self.map_sprite = pygame.image.load('./assets/map.png').convert_alpha()
        self.map_sprite.set_colorkey((0,0,0))



    def init_map(self):
        m = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,],
            [1,2,1,0,0,1,2,1,0,0,0,1,2,1,1,2,1,0,0,0,1,2,1,0,0,1,2,1,],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,],
            [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,],
            [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,],
            [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1,],
            [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1,],
            [0,0,0,0,0,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,0,0,0,0,0,],
            [0,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,0,],
            [0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0,],
            [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1,],
            [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0,],
            [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1,],
            [0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0,],
            [0,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,0,],
            [0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0,],
            [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1,],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,],
            [1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,1,],
            [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,],
            [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,],
            [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1,],
            [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,],
            [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
        ]
        return m

    


    def draw(self):
        fblits = []
        fblits.append((self.map_sprite, (0, 0, TILE_SIZE*TILE_HORIZONTAL, TILE_SIZE*GAME_TILE_VERTICAL)))

        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell == 2:
                    fblits.append((self.tiles["pellet"], (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)))

        return fblits
    


    def get_rects(self):
        rects = {"wall": [], "pellet": [],}
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                cell_rect = (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if cell == 2:
                    rects["pellet"].append(cell_rect)
                elif cell == 1:
                    rects["wall"].append(cell_rect)
        return rects
    


    def pellet_collision(self, collision):
        if not collision: return
        collision_tile_x = collision[0] // TILE_SIZE
        collision_tile_y = collision[1] // TILE_SIZE
        if self.map[collision_tile_y][collision_tile_x] == 2:
            self.map[collision_tile_y][collision_tile_x] = 0
        return