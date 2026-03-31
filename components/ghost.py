import pygame, math
from src.settings import *



class Ghost():
    def __init__(self):
        self.name = ""
        self.state = "scatter"
        
        self.sprites = {}

        self.width, self.height = 8, 8
        self.surface_width, self.surface_height = 16, 16

        self.pos = pygame.Vector2()
        self.dir = pygame.Vector2()
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 8, 8)
        self.target = pygame.Vector2()

        self.sprite_dir = "up"
        self.framecount = 0
        self.anim_frame = 1


    
    def update(self, map, collrects, dt):

        # Movement
        
        self.pos.x += GHOST_SPEED * self.dir.x * dt
        collision = self.check_collision(collrects)

        if collision and self.dir.x:
            self.pos.x = collision[0] - (self.rect.width * self.dir.x)
            self.dir.x = 0


        self.pos.y += GHOST_SPEED * self.dir.y * dt
        collision = self.check_collision(collrects)
        
        if collision and self.dir.y:
            self.pos.y = collision[1] - (self.rect.height * self.dir.y)
            self.dir.y = 0


        if self.pos.x <= -self.rect.width - 1:
            self.pos.x = GAME_SIZE[0]
            self.pos.y = 14*TILE_SIZE
        if self.pos.x >= GAME_SIZE[0] + 1:
            self.pos.x = -self.rect.width
            self.pos.y = 14*TILE_SIZE


        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


        if self.dir.x > 0:
            self.sprite_dir = "right"
        if self.dir.x < 0:
            self.sprite_dir = "left"
        if self.dir.y > 0:
            self.sprite_dir = "down"
        if self.dir.y < 0:
            self.sprite_dir = "up"

        if self.framecount >= 10:
            self.framecount = 0
            match self.anim_frame:
                case 1: self.anim_frame = 2
                case 2: self.anim_frame = 1
        self.framecount += 1


        self.surface = self.sprites[f"{self.sprite_dir}-{self.anim_frame}"]


        # Change Direction

        simple_pos = (math.floor(self.pos.x // TILE_SIZE), math.floor(self.pos.y // TILE_SIZE))

        dirs = [
            [(0,-1), (simple_pos[0], simple_pos[1] - 1)],
            [(-1,0), (simple_pos[0] - 1, simple_pos[1])],
            [(0,1), (simple_pos[0], simple_pos[1] + 1)],
            [(1,0), (simple_pos[0] + 1, simple_pos[1])],
        ]

        checked_squares = []

        # Check for valid move squares
        for dir in dirs:

            try:
                dir.append(map[dir[1][1]][dir[1][0]])
            except:
                dir.append(0)
            
            if (dir[0][0] * -1 == self.dir.x and self.dir.x != 0) or (dir[0][1] * -1 == self.dir.y and self.dir.y != 0):
                checked_squares.append(None)
                continue

            if dir[2] != 1:
                checked_squares.append(dir[1])
            else:
                checked_squares.append(None)
        
        change_dir = (None, 2000000)
        for i, square in enumerate(checked_squares):
            if square == None: continue
            square_dist = (self.target[0] - square[0])**2 + (self.target[1] - square[1])**2
            if square_dist < change_dir[1]:
                change_dir = (dirs[i][0], square_dist)

        if change_dir[0]:
            self.dir.x = change_dir[0][0] if change_dir[0][0] != 0 else self.dir.x
            self.dir.y = change_dir[0][1] if change_dir[0][1] != 0 else self.dir.y
    


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
    


    def draw(self):
        blits = [
            (self.surface, (self.pos.x - self.width / 2, self.pos.y - self.width / 2, self.surface_width, self.surface_height)),
        ]
        return blits