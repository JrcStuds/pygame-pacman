import pygame

GOD_MODE = True
SHOW_GHOST_TARGETS = False

TILE_HORIZONTAL = 28
GAME_TILE_VERTICAL = 31
DISPLAY_TILE_VERTICAL = 36
TILE_SIZE = 8
GAME_SIZE = (TILE_HORIZONTAL * TILE_SIZE, GAME_TILE_VERTICAL * TILE_SIZE)
DISPLAY_SIZE = (TILE_HORIZONTAL * TILE_SIZE, DISPLAY_TILE_VERTICAL * TILE_SIZE)

PLAYER_SPEED = 80
GHOST_SPEED = 65
GHOST_HOME_SPEED = 40
GHOST_TRANSITION_SPEED = 10

PELLET_SCORE = 10

TILESET_SPRITES = {
    "pacman-closed": pygame.Rect(32, 0, 16, 16),
    "pacman-right-1": pygame.Rect(0, 0, 16, 16),
    "pacman-right-2": pygame.Rect(16, 0, 16, 16),
    "pacman-left-1": pygame.Rect(0, 16, 16, 16),
    "pacman-left-2": pygame.Rect(16, 16, 16, 16),
    "pacman-up-1": pygame.Rect(0, 32, 16, 16),
    "pacman-up-2": pygame.Rect(16, 32, 16, 16),
    "pacman-down-1": pygame.Rect(0, 48, 16, 16),
    "pacman-down-2": pygame.Rect(16, 48, 16, 16),
    "pacman-death-0": pygame.Rect(48, 0, 16, 16),
    "pacman-death-1": pygame.Rect(64, 0, 16, 16),
    "pacman-death-2": pygame.Rect(80, 0, 16, 16),
    "pacman-death-3": pygame.Rect(96, 0, 16, 16),
    "pacman-death-4": pygame.Rect(112, 0, 16, 16),
    "pacman-death-5": pygame.Rect(128, 0, 16, 16),
    "pacman-death-6": pygame.Rect(144, 0, 16, 16),
    "pacman-death-7": pygame.Rect(160, 0, 16, 16),
    "pacman-death-8": pygame.Rect(176, 0, 16, 16),
    "pacman-death-9": pygame.Rect(192, 0, 16, 16),
    "pacman-death-10": pygame.Rect(208, 0, 16, 16),
    "blinky-right-1": pygame.Rect(0, 64, 16, 16),
    "blinky-right-2": pygame.Rect(16, 64, 16, 16),
    "blinky-left-1": pygame.Rect(32, 64, 16, 16),
    "blinky-left-2": pygame.Rect(48, 64, 16, 16),
    "blinky-up-1": pygame.Rect(64, 64, 16, 16),
    "blinky-up-2": pygame.Rect(80, 64, 16, 16),
    "blinky-down-1": pygame.Rect(96, 64, 16, 16),
    "blinky-down-2": pygame.Rect(112, 64, 16, 16),
    "pinky-right-1": pygame.Rect(0, 80, 16, 16),
    "pinky-right-2": pygame.Rect(16, 80, 16, 16),
    "pinky-left-1": pygame.Rect(32, 80, 16, 16),
    "pinky-left-2": pygame.Rect(48, 80, 16, 16),
    "pinky-up-1": pygame.Rect(64, 80, 16, 16),
    "pinky-up-2": pygame.Rect(80, 80, 16, 16),
    "pinky-down-1": pygame.Rect(96, 80, 16, 16),
    "pinky-down-2": pygame.Rect(112, 80, 16, 16),
    "inky-right-1": pygame.Rect(0, 96, 16, 16),
    "inky-right-2": pygame.Rect(16, 96, 16, 16),
    "inky-left-1": pygame.Rect(32, 96, 16, 16),
    "inky-left-2": pygame.Rect(48, 96, 16, 16),
    "inky-up-1": pygame.Rect(64, 96, 16, 16),
    "inky-up-2": pygame.Rect(80, 96, 16, 16),
    "inky-down-1": pygame.Rect(96, 96, 16, 16),
    "inky-down-2": pygame.Rect(112, 96, 16, 16),
    "clyde-right-1": pygame.Rect(0, 112, 16, 16),
    "clyde-right-2": pygame.Rect(16, 112, 16, 16),
    "clyde-left-1": pygame.Rect(32, 112, 16, 16),
    "clyde-left-2": pygame.Rect(48, 112, 16, 16),
    "clyde-up-1": pygame.Rect(64, 112, 16, 16),
    "clyde-up-2": pygame.Rect(80, 112, 16, 16),
    "clyde-down-1": pygame.Rect(96, 112, 16, 16),
    "clyde-down-2": pygame.Rect(112, 112, 16, 16),
    "ghost-scared-blue-1": pygame.Rect(128, 64, 16, 16),
    "ghost-scared-blue-2": pygame.Rect(144, 64, 16, 16),
    "ghost-scared-white-1": pygame.Rect(160, 64, 16, 16),
    "ghost-scared-white-2": pygame.Rect(176, 64, 16, 16),
    "ghost-eyes-right": pygame.Rect(128, 80, 16, 16),
    "ghost-eyes-left": pygame.Rect(144, 80, 16, 16),
    "ghost-eyes-up": pygame.Rect(160, 80, 16, 16),
    "ghost-eyes-down": pygame.Rect(176, 80, 16, 16),
}

TILESET_TEXT = {
    "a": pygame.Rect(0, 0, 8, 8),
    "b": pygame.Rect(8, 0, 8, 8),
    "c": pygame.Rect(16, 0, 8, 8),
    "d": pygame.Rect(24, 0, 8, 8),
    "e": pygame.Rect(32, 0, 8, 8),
    "f": pygame.Rect(40, 0, 8, 8),
    "g": pygame.Rect(48, 0, 8, 8),
    "h": pygame.Rect(56, 0, 8, 8),
    "i": pygame.Rect(64, 0, 8, 8),
    "j": pygame.Rect(72, 0, 8, 8),
    "k": pygame.Rect(80, 0, 8, 8),
    "l": pygame.Rect(88, 0, 8, 8),
    "m": pygame.Rect(96, 0, 8, 8),
    "n": pygame.Rect(104, 0, 8, 8),
    "o": pygame.Rect(112, 0, 8, 8),
    "p": pygame.Rect(0, 8, 8, 8),
    "q": pygame.Rect(8, 8, 8, 8),
    "r": pygame.Rect(16, 8, 8, 8),
    "s": pygame.Rect(24, 8, 8, 8),
    "t": pygame.Rect(32, 8, 8, 8),
    "u": pygame.Rect(40, 8, 8, 8),
    "v": pygame.Rect(48, 8, 8, 8),
    "w": pygame.Rect(56, 8, 8, 8),
    "x": pygame.Rect(64, 8, 8, 8),
    "y": pygame.Rect(72, 8, 8, 8),
    "z": pygame.Rect(80, 8, 8, 8),
    "!": pygame.Rect(88, 8, 8, 8),
    "0": pygame.Rect(0, 16, 8, 8),
    "1": pygame.Rect(8, 16, 8, 8),
    "2": pygame.Rect(16, 16, 8, 8),
    "3": pygame.Rect(24, 16, 8, 8),
    "4": pygame.Rect(32, 16, 8, 8),
    "5": pygame.Rect(40, 16, 8, 8),
    "6": pygame.Rect(48, 16, 8, 8),
    "7": pygame.Rect(56, 16, 8, 8),
    "8": pygame.Rect(64, 16, 8, 8),
    "9": pygame.Rect(72, 16, 8, 8),
}

SCATTER_TILES = {
    "blinky": pygame.Vector2(25, -3),
    "pinky": pygame.Vector2(2, -3),
    "inky": pygame.Vector2(27, 32),
    "clyde": pygame.Vector2(0, 32),
}

START_TILES = {
    "blinky": pygame.Vector2(13, 11),
    "pinky": pygame.Vector2(13.5, 14.5),
    "inky": pygame.Vector2(11.5, 13.5),
    "clyde": pygame.Vector2(15.5, 13.5),
}

HOME_COUNTER = {
    "blinky": 0,
    "pinky": 0,
    "inky": 100,
    "clyde": 150,
}

GHOST_COLOURS = {
    "blinky": "red",
    "pinky": "pink",
    "inky": "cyan",
    "clyde": "orange",
}

DIRECTIONS = {
    (0, 1): "down",
    (0, -1): "up",
    (1, 0): "right",
    (-1, 0): "left",
}

INTERSECTION_TILES = [
    pygame.Vector2(6, 1),
    pygame.Vector2(21, 1),
    pygame.Vector2(1, 5),
    pygame.Vector2(6, 5),
    pygame.Vector2(9, 5),
    pygame.Vector2(12, 5),
    pygame.Vector2(15, 5),
    pygame.Vector2(18, 5),
    pygame.Vector2(21, 5),
    pygame.Vector2(26, 5),
    pygame.Vector2(6, 8),
    pygame.Vector2(21, 8),
    pygame.Vector2(12, 11),
    pygame.Vector2(15, 11),
    pygame.Vector2(6, 14),
    pygame.Vector2(9, 14),
    pygame.Vector2(18, 14),
    pygame.Vector2(21, 14),
    pygame.Vector2(9, 17),
    pygame.Vector2(18, 17),
    pygame.Vector2(6, 20),
    pygame.Vector2(9, 20),
    pygame.Vector2(18, 20),
    pygame.Vector2(21, 20),
    pygame.Vector2(6, 23),
    pygame.Vector2(9, 23),
    pygame.Vector2(12, 23),
    pygame.Vector2(15, 23),
    pygame.Vector2(18, 23),
    pygame.Vector2(21, 23),
    pygame.Vector2(3, 26),
    pygame.Vector2(24, 26),
    pygame.Vector2(12, 29),
    pygame.Vector2(15, 29),
]

SPECIAL_INTERSECTION_TILES = [
    pygame.Vector2(12, 11),
    pygame.Vector2(15, 11),
    pygame.Vector2(12, 23),
    pygame.Vector2(15, 23),
]