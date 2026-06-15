import pygame
from Galaxy import GenerateStars
import random as rn
import config
import civ



pygame.init()

screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Universe Civ Sim")
clock = pygame.time.Clock()
civ.handleCiv
clock.tick(60)

WindowSize = pygame.display.get_window_size()
WindowHeight = WindowSize[0]
print(WindowHeight)
WindowWidth = WindowSize[1]

GenerateStars(rn.randrange(config.MinStar, config.MaxStar), screen, WindowHeight, WindowWidth, 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit

print("Generating Stars")