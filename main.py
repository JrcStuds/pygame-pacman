import pygame
from core.settings import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()
dt = 0


sprites = {}
sprites["pacman"] = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
pygame.draw.circle(sprites["pacman"], "yellow", (TILE_SIZE / 2, TILE_SIZE / 2), TILE_SIZE / 2)


pos = {}
pos["pacman"] = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

pacman_dir = pygame.Vector2(0, 0)



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")
    fblits = []

    fblits.append((sprites["pacman"], pos["pacman"]))


    keys = pygame.key.get_pressed()
    pos["pacman"].x += (keys[pygame.K_d] - keys[pygame.K_a]) * PACMAN_SPEED * dt
    pos["pacman"].y += (keys[pygame.K_s] - keys[pygame.K_w]) * PACMAN_SPEED * dt


    screen.fblits(fblits)

    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()