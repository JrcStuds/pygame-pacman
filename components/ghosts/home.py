import pygame


class Home():
    def __init__(self):
        pass


    def get_sprite(self, framecount):
        if framecount % 20 < 10:
            return ["dir", "1"]
        else:
            return ["dir", "2"]