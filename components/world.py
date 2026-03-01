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



    def init_map(self):
        """
        0 - empty
        1 - pellet
        2 - thin wall
        3 - thick wall
        4 - square wall
        5 - gate
        """
        m = [
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,],
            [3,1,1,1,1,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,3,],
            [3,1,2,2,2,2,1,2,2,2,2,2,1,3,3,1,2,2,2,2,2,1,2,2,2,2,1,3,],
            [3,1,2,2,2,2,1,2,2,2,2,2,1,3,3,1,2,2,2,2,2,1,2,2,2,2,1,3,],
            [3,1,2,2,2,2,1,2,2,2,2,2,1,3,3,1,2,2,2,2,2,1,2,2,2,2,1,3,],
            [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,],
            [3,1,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,3,],
            [3,1,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,3,],
            [3,1,1,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,1,1,3,],
            [3,3,3,3,3,3,1,2,2,2,2,2,0,2,2,0,2,2,2,2,2,1,3,3,3,3,3,3,],
            [0,0,0,0,0,3,1,2,2,2,2,2,0,2,2,0,2,2,2,2,2,1,3,0,0,0,0,0,],
            [0,0,0,0,0,3,1,2,2,0,0,0,0,0,0,0,0,0,0,2,2,1,3,0,0,0,0,0,],
            [0,0,0,0,0,3,1,2,2,0,4,4,5,5,5,5,4,4,0,2,2,1,3,0,0,0,0,0,],
            [3,3,3,3,3,3,1,2,2,0,4,0,0,0,0,0,0,4,0,2,2,1,3,3,3,3,3,3,],
            [0,0,0,0,0,0,1,0,0,0,4,0,0,0,0,0,0,4,0,0,0,1,0,0,0,0,0,0,],
            [3,3,3,3,3,3,1,2,2,0,4,0,0,0,0,0,0,4,0,2,2,1,3,3,3,3,3,3,],
            [0,0,0,0,0,3,1,2,2,0,4,4,4,4,4,4,4,4,0,2,2,1,3,0,0,0,0,0,],
            [0,0,0,0,0,3,1,2,2,0,0,0,0,0,0,0,0,0,0,2,2,1,3,0,0,0,0,0,],
            [0,0,0,0,0,3,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,3,0,0,0,0,0,],
            [3,3,3,3,3,3,1,2,2,0,2,2,2,2,2,2,2,2,0,2,2,1,3,3,3,3,3,3,],
            [3,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,],
            [3,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,3,],
            [3,1,2,2,2,2,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,1,2,2,2,2,1,3,],
            [3,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,3,],
            [3,3,3,1,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,1,3,3,3,],
            [3,3,3,1,2,2,1,2,2,1,2,2,2,2,2,2,2,2,1,2,2,1,2,2,1,3,3,3,],
            [3,1,1,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,2,2,1,1,1,1,1,1,3,],
            [3,1,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,1,3,],
            [3,1,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,1,3,],
            [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,],
        ]
        return m

    


    def draw(self):
        fblits = []
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                pos = (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)

                match cell:
                    case 0: 
                        fblits.append((self.tiles["blank"], pos))
                    case 1: 
                        fblits.append((self.tiles["pellet"], pos))
                    case 2: pass
                    case 3: pass
                    case 4: pass
                    case 5: 
                        if self.map[i][j-1] != 5:
                            fblits.append((self.tiles["left-gate"], pos))
                        elif self.map[i][j+1] != 5:
                            fblits.append((self.tiles["right-gate"], pos))
                        else:
                            fblits.append((self.tiles["main-gate"], pos))

        return fblits
    


    def get_rects(self):
        rects = {"wall": [], "pellet": [],}
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                cell_rect = (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                match cell:
                    case 1: rects["wall"].append(cell_rect)
                    case 2: rects["pellet"].append(cell_rect)
        return rects
    


    def pellet_collision(self, collision):
        if not collision: return
        collision_tile_x = collision[0] // TILE_SIZE
        collision_tile_y = collision[1] // TILE_SIZE
        if self.map[collision_tile_y][collision_tile_x] == 2:
            self.map[collision_tile_y][collision_tile_x] = 0
        return