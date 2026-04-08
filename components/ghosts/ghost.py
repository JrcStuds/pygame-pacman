import pygame
from src.settings import *
from .scatter import Scatter


class Ghost():
    def __init__(self, name, game):
        self.tileset = pygame.image.load('./assets/sprites.png').convert()
        self.tileset.set_colorkey((0, 0, 0))

        self.sprites = self.init_sprites(name)
        self.scatter_tile = SCATTER_TILES[name]

        self.game = game

        self.states = {
            "chase": None,
            "scatter": Scatter(),
            "frightened": None,
            "eaten": None,
            "home": None,
        }
        self.current_state = "scatter"


        self.width, self.height = 8, 8
        self.surface_width, self.surface_height = 16, 16

        self.pos = pygame.Vector2(8, 8)
        self.dir = pygame.Vector2(0, 1)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 8, 8)
        self.target = pygame.Vector2()

        self.framecount = 0
        self.last_tile = None
    


    def update(self):
        self.framecount = 0 if self.framecount >= 59 else self.framecount + 1

        if hasattr(self.states[self.current_state], "get_target"):
            self.target = self.states[self.current_state].get_target(ghost=self, game=self.game)
        
        self.move()
    


    def draw(self):
        if hasattr(self.states[self.current_state], "get_sprite"):
            new_sprite = self.states[self.current_state].get_sprite(self.framecount)
            sprite = self.parse_sprite(new_sprite)
            sprite_pos = pygame.Vector2(
                self.pos.x - (self.surface_width - self.width) / 2,
                self.pos.y - (self.surface_height - self.height) / 2,
            )
            return [(sprite, sprite_pos)]
        
        else:
            return []
        

    
    def parse_sprite(self, sprite_list):
        for i, arg in enumerate(sprite_list):
            if arg == "dir":
                sprite_list[i] = DIRECTIONS[(self.dir.x, self.dir.y)]
        sprite = self.sprites["-".join(sprite_list)]
        return sprite
        


    def move(self):
        tile = round(self.pos / 8)
        if (
            (
                tile in INTERSECTION_TILES or
                self.game.world.map[int(tile.y + self.dir.y)][int(tile.x + self.dir.x)] == 1   # the tile in front of ghost is a wall
            ) and
            (self.pos - tile * 8).length() < (GHOST_SPEED * self.game.dt) and   # within one frame's movement of the centre of the square
            tile != self.last_tile
        ):
            special_intersection = True if tile in SPECIAL_INTERSECTION_TILES else False
            self.last_tile = tile
            self.change_dir(special_intersection)
        
        # move by GHOST_SPEED in current direction
        self.pos += self.dir * GHOST_SPEED * self.game.dt



    def change_dir(self, special_intersection):
        tile = round(self.pos / 8)

        # find all of the valid directions ghost can go
        potential_dirs = [
            pygame.Vector2(0, -1),
            pygame.Vector2(-1, 0),
            pygame.Vector2(0, 1),
            pygame.Vector2(1, 0),
        ]
        valid_dirs = []
        for dir in potential_dirs:
            # skip up if special intersection
            if special_intersection and dir ==  pygame.Vector2(0, -1):
                continue

            # skip reverse direction
            if dir == self.dir * -1:
                continue
            
            # skip if tile is a wall
            check_tile = tile + dir
            if self.game.world.map[int(check_tile.y)][int(check_tile.x)] == 1:
                continue
            
            valid_dirs.append(dir)
        
        # set the best dir to the current, and check each valid directions for if they are better
        best_direction = None
        if valid_dirs:
            for dir in valid_dirs:
                if not best_direction:
                    best_direction = dir
                elif self.target.distance_to(tile + dir) < self.target.distance_to(tile + best_direction):
                    best_direction = dir
        
        # snap to centre of tile
        if best_direction != self.dir:
            self.pos = tile * TILE_SIZE
            self.dir = best_direction

    

    def init_sprites(self, name):
        sprites = {}
        for sprite in TILESET_SPRITES.keys():
            if sprite[:len(name)] == name:
                sprites[sprite[ len(name) + 1:]] = self.tileset.subsurface(TILESET_SPRITES[sprite])
        return sprites