import pygame
from Galaxy import GenerateStars
import random as rn
import config
import civ


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
CivLayer = pygame.display.set_mode((1000, 1000))
CivLayer.set_alpha(50)
pygame.display.set_caption("Universe Civ Sim")
clock = pygame.time.Clock()
WindowSize = pygame.display.get_window_size()
WindowHeight = WindowSize[0]
print(WindowHeight)
WindowWidth = WindowSize[1]

GenerateStars(rn.randrange(config.ReadSetting(7), config.ReadSetting(8)), screen, WindowHeight, WindowWidth)
running = True
ADVANCE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADVANCE_EVENT, 100)
while running:
    for events in pygame.event.get():
        if events.type == ADVANCE_EVENT:
            for civilization in civ.alive:
                civilization.Advance(CivLayer)
        if events.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()