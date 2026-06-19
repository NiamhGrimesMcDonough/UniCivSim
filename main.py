import pygame
from Galaxy import GenerateStars
import random as rn
import config
import civ



pygame.init()

screen = pygame.display.set_mode((1000, 1000))
CivLayer = pygame.display.set_mode((1000, 1000))
CivLayer.set_alpha(150)
pygame.display.set_caption("Universe Civ Sim")
clock = pygame.time.Clock()
WindowSize = pygame.display.get_window_size()
WindowHeight = WindowSize[0]
print(WindowHeight)
WindowWidth = WindowSize[1]

GenerateStars(rn.randrange(config.MinStar, config.MaxStar), screen, WindowHeight, WindowWidth, 0)
running = True
ADVANCE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADVANCE_EVENT, 100)
while running:
    for event in pygame.event.get():
        if event.type == ADVANCE_EVENT:
            for civilization in civ.alive:
                civilization.Advance(CivLayer)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()