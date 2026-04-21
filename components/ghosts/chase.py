import pygame
from src.settings import *


class Chase():
    def __init__(self):
        pass


    def get_sprite(self, framecount):
        if framecount % 20 < 10:
            return ["dir", "1"]
        else:
            return ["dir", "2"]
        

    def get_target(self, ghost, game):
        match ghost.name:
            case "blinky": return self.blinky_get_target(game)
            case "pinky": return self.pinky_get_target(game)
            case "inky": return self.inky_get_target(ghost, game)
            case "clyde": return self.clyde_get_target(ghost, game)
    

    def blinky_get_target(self, game):
        target = round(game.player.pos / TILE_SIZE)
        return target
    

    def pinky_get_target(self, game):
        player_tile = round(game.player.pos / TILE_SIZE)
        tile_offset = game.player.dir * 4
        target = player_tile + tile_offset
        return target
    

    def inky_get_target(self, ghost, game):
        player_tile = round(game.player.pos / TILE_SIZE)
        tile_offset = game.player.dir * 2
        blinky_tile = pygame.Vector2()
        for ghost in game.ghosts:
            if ghost.name == "blinky":
                blinky_tile = round(ghost.pos / TILE_SIZE)
        blinky_dist = blinky_tile - (player_tile + tile_offset)
        target = (player_tile + tile_offset) - blinky_dist
        return target
    

    def clyde_get_target(self, ghost, game):
        player_tile = round(game.player.pos / TILE_SIZE)
        ghost_tile = round(ghost.pos / TILE_SIZE)
        if player_tile.distance_to(ghost_tile) > 8:
            target = player_tile
        else:
            target = ghost.scatter_tile
        return target