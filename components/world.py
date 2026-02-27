import pygame
from src.settings import *


class World:
    def __init__(self, tilset):
        self.tiles = self.init_tiles()
        self.map = self.init_map()



    def init_tiles(self):
        # 0x = full colour
        # 1x = side
        # 2x = outer corner
        # 3x = inner corner
        # 4x = misc
        tiles = {}

        tiles[0] = pygame.Surface((TILE_SIZE, TILE_SIZE)) # empty
        tiles[0].fill("black")

        tiles[1] = pygame.Surface((TILE_SIZE, TILE_SIZE)) # wall
        tiles[1].fill("blue")

        tiles[2] = pygame.Surface((TILE_SIZE, TILE_SIZE)) # pellet
        tiles[2].fill("black")
        pygame.draw.rect(
            tiles[2],
            "white",
            (
                TILE_SIZE * (3 / 8),
                TILE_SIZE * (3 / 8),
                TILE_SIZE / 4,
                TILE_SIZE / 4
            )
        )

        tiles[3] = pygame.Surface((TILE_SIZE, TILE_SIZE))
        tiles[3].fill("black")
        pygame.draw.rect(
            tiles[3],
            "blue",
            (
                TILE_SIZE / 2,
                TILE_SIZE / 2,
                TILE_SIZE / 2,
                TILE_SIZE / 2
            )
        )

        tiles[4] = pygame.Surface((TILE_SIZE, TILE_SIZE))
        tiles[4].fill("black")
        pygame.draw.rect(
            tiles[4],
            "blue",
            (
                0,
                TILE_SIZE / 2,
                TILE_SIZE / 2,
                TILE_SIZE / 2
            )
        )

        return tiles



    def init_map(self):
        m = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1,],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,],
            [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,],
            [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1,],
            [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1,],
            [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1,],
            [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1,],
            [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1,],
            [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1,],
            [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1,],
            [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0,],
            [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1,],
            [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1,],
            [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1,],
            [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1,],
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
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                fblits.append((self.tiles[cell], (j*TILE_SIZE, i*TILE_SIZE, TILE_SIZE, TILE_SIZE)))
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