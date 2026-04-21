import pygame
from src.settings import *
from .scatter import Scatter
from .chase import Chase
from .home import Home


class Ghost():
    def __init__(self, name, game):
        self.tileset = pygame.image.load('./assets/sprites.png').convert()
        self.tileset.set_colorkey((0, 0, 0))

        self.name = name
        self.sprites = self.init_sprites(name)
        self.scatter_tile = SCATTER_TILES[name]

        self.game = game

        self.states = {
            "chase": Chase(),
            "scatter": Scatter(),
            "frightened": None,
            "eaten": None,
            "home": Home(),
            "transition": Home(),
        }
        self.current_state = "chase" if self.name == "blinky" else "home"


        self.width, self.height = 8, 8
        self.surface_width, self.surface_height = 16, 16

        self.pos = START_TILES[self.name] * TILE_SIZE
        self.dir = pygame.Vector2(0, 1)
        self.rect = pygame.Rect()
        self.target = pygame.Vector2()

        self.framecount = 0
        self.state_timer = 0

        self.last_tile = None
    


    def update(self):
        self.framecount = 0 if self.framecount >= 59 else self.framecount + 1
        self.state_timer += 1

        if self.current_state == "home":
            self.move_home()
            return
        
        if self.current_state == "transition":
            self.transition_from_home()
            return

        match self.current_state:
            case "home":
                self.move_home()
                return
            case "transition":
                self.transition_from_home()
                return
            case _:
                if self.current_state != self.game.ghost_state_timer[1]:
                    self.current_state = self.game.ghost_state_timer[1]

        if hasattr(self.states[self.current_state], "get_target"):
            self.target = self.states[self.current_state].get_target(ghost=self, game=self.game)
        
        self.move()

        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
    


    def draw(self):
        blits = []

        if hasattr(self.states[self.current_state], "get_sprite"):
            new_sprite = self.states[self.current_state].get_sprite(self.framecount)
            sprite = self.parse_sprite(new_sprite)
            sprite_pos = pygame.Vector2(
                self.pos.x - (self.surface_width - self.width) / 2,
                self.pos.y - (self.surface_height - self.height) / 2,
            )
            blits.append((sprite, sprite_pos))

        if SHOW_GHOST_TARGETS:
            s = pygame.Surface((8,8))
            s.fill(GHOST_COLOURS[self.name])
            if (0 <= self.target.x <= DISPLAY_SIZE[0] and 0 <= self.target.y <= DISPLAY_SIZE[1]): blits.append((s, self.target * 8))
        
        return blits
        

    
    def parse_sprite(self, sprite_list):
        for i, arg in enumerate(sprite_list):
            if arg == "dir":
                sprite_list[i] = DIRECTIONS[(self.dir.x, self.dir.y)]
        sprite = self.sprites["-".join(sprite_list)]
        return sprite
        


    def move(self):
        tile = round(self.pos / TILE_SIZE)
        
        # check if facing wall before doing other checks (for errors)
        facing_wall = False
        if 0 <= tile.x + self.dir.x < TILE_HORIZONTAL:   # tile in front of ghost exists
            if self.game.world.map[int(tile.y + self.dir.y)][int(tile.x + self.dir.x)] == 1:   # tile in front of ghost is wall 
                facing_wall = True

        if (
            (tile in INTERSECTION_TILES or facing_wall) and
            (self.pos - tile * TILE_SIZE).length() < (GHOST_SPEED * self.game.dt) and   # within one frame's movement of the centre of the square
            tile != self.last_tile
        ):
            special_intersection = True if tile in SPECIAL_INTERSECTION_TILES else False
            self.last_tile = tile
            self.change_dir(special_intersection)
        
        # move by GHOST_SPEED in current direction
        self.pos += self.dir * GHOST_SPEED * self.game.dt

        # screen looping
        if self.pos.x < -self.surface_width:
            self.pos.x = TILE_HORIZONTAL * TILE_SIZE
        if self.pos.x > TILE_HORIZONTAL * TILE_SIZE:
            self.pos.x = -self.surface_width



    def change_dir(self, special_intersection):
        tile = round(self.pos / TILE_SIZE)

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



    def move_home(self):
        if self.game.header.score >= HOME_COUNTER[self.name] * PELLET_SCORE:
            self.pos.y = 14 * TILE_SIZE
            self.current_state = "transition"
            return
        
        if self.pos.y / TILE_SIZE > 14.5:
            self.dir *= -1
            self.pos.y = 14.5 * TILE_SIZE
        if self.pos.y / TILE_SIZE < 13.5:
            self.dir *= -1
            self.pos.y = 13.5 * TILE_SIZE
        
        self.pos += self.dir * GHOST_HOME_SPEED * self.game.dt
    

    def transition_from_home(self):
        centre_home = (pygame.Vector2(13.5, 14) * TILE_SIZE)
        target_outside = (pygame.Vector2(13.5, 11) * TILE_SIZE)
        if abs(self.pos.x - centre_home.x) > GHOST_TRANSITION_SPEED * self.game.dt:
            self.dir = (centre_home - self.pos).normalize()
        elif abs(target_outside.y - self.pos.y) > GHOST_TRANSITION_SPEED * self.game.dt:
            self.dir = pygame.Vector2(0, -1)
        else:
            self.current_state = "scatter"
            self.dir = pygame.Vector2(1, 0)
            self.pos = target_outside
        self.pos += self.dir * GHOST_TRANSITION_SPEED * self.game.dt