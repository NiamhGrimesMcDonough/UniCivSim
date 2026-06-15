import random as rn
import config
import pygame

class Star:
    def __init__(self, colour, xy, size, ID):
        self.colour = colour
        self.xy = xy
        self.size = size
        self.id = ID

def GenerateStars(stars_remaining, surface, WindowHeight, WindowWidth):
    if stars_remaining <= 0:
        print("Stars Generated!")
        return
    while stars_remaining >= 1:
        x= rn.randrange(0,WindowHeight)
        y= rn.randrange(0,WindowWidth)
        xy = (x, y)
        star = Star("White", xy, 1, stars_remaining)
        pygame.draw.circle(surface, star.colour, xy, star.size)
        stars_remaining -= 1
        print (stars_remaining)