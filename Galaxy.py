import random as rn
import config
import pygame
import civ

class Star:
    def __init__(self, colour, xy, size, ID):
        self.colour = colour
        self.xy = xy
        self.size = size
        self.id = ID

def GenerateStars(stars_remaining, surface, WindowHeight, WindowWidth, NoOfCivs):
    if stars_remaining <= 0:
        print("Stars Generated!")
        return
    while stars_remaining >= 1:
        StarColours = ["Blue", "Yellow", "White", "Red"]
        c= rn.choices(StarColours, weights=[1, 10, 10, 5], k=1)
        colour = "".join(str(x) for x in c)
        s= rn.randrange(1,4)
        x= rn.randrange(0,WindowHeight)
        y= rn.randrange(0,WindowWidth)
        xy = (x, y)
        lifeRoll = rn.randrange(0, 100)
        if lifeRoll <= config.CivProbability*100:
            NoOfCivs += 1
            civ.spawnCiv(xy, NoOfCivs)
        star = Star(colour, xy, s, stars_remaining)
        pygame.draw.circle(surface, star.colour, xy, star.size)
        stars_remaining -= 1