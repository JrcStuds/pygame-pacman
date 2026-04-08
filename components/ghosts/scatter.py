import pygame


class Scatter():
    def __init__(self):
        pass


    
    def get_sprite(self, framecount):
        if framecount % 20 < 10:
            return ["dir", "1"]
        else:
            return ["dir", "2"]
        


    def get_target(self, ghost, game):
        return pygame.Vector2(ghost.scatter_tile)