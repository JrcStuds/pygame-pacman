import pygame
from src.settings import *


class Player():
    def __init__(self):
        self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, "yellow", (TILE_SIZE / 2, TILE_SIZE / 2), TILE_SIZE / 2,)
        self.pos = pygame.Vector2(8, 8)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.surface.get_width(), self.surface.get_height())

        self.dir = pygame.Vector2(0, 0)
    


    def draw(self):
        return (self.surface, self.rect)
    


    def update(self, keys, collrects, dt):

        if keys["up"]:
            self.dir.y = -1
        if keys["down"]:
            self.dir.y = 1
        if keys["left"]:
            self.dir.x = -1
        if keys["right"]:
            self.dir.x = 1


        self.pos.x += PLAYER_SPEED * self.dir.x * dt
        collision = self.check_collision(collrects)
        if collision and self.dir.x:
            self.pos.x = collision[0] - (self.rect.width * self.dir.x)
            self.dir.x = 0
            

        self.pos.y += PLAYER_SPEED * self.dir.y * dt
        collision = self.check_collision(collrects)
        if collision and self.dir.y:
            self.pos.y = collision[1] - (self.rect.height * self.dir.y)
            self.dir.y = 0


        if self.pos.x <= -self.rect.width - 1:
            self.pos.x = SCREEN_WIDTH
            self.pos.y = 14*TILE_SIZE
        if self.pos.x >= SCREEN_WIDTH + 1:
            self.pos.x = -self.rect.width
            self.pos.y = 14*TILE_SIZE

        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
    


    def check_pellet_collision(self, rects):
        collision = self.check_collision(rects)
        return collision



    def check_collision(self, rects):
        player_sides = {
            "top": self.pos.y,
            "bottom": self.pos.y + self.rect.height - 1,
            "left": self.pos.x,
            "right": self.pos.x + self.rect.width - 1,
        }
        for rect in rects:
            rect_sides = {
                "top": rect[1],
                "bottom": rect[1] + rect[3] - 1,
                "left": rect[0],
                "right": rect[0] + rect[2] - 1,
            }
            if (
                ((rect_sides["top"] <= player_sides["top"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["left"] <= rect_sides["right"])) or
                ((rect_sides["top"] <= player_sides["top"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["right"] <= rect_sides["right"])) or
                ((rect_sides["top"] <= player_sides["bottom"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["left"] <= rect_sides["right"])) or
                ((rect_sides["top"] <= player_sides["bottom"] <= rect_sides["bottom"]) and (rect_sides["left"] <= player_sides["right"] <= rect_sides["right"]))
            ):
                return rect
        return None