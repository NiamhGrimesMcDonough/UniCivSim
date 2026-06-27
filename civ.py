import pygame
import random as rn
alive = pygame.sprite.Group()
def spawnCiv(xy):
    civilization = Civ(CivColour(), xy, 10, rn.randrange(1, 99900)/100000)
    

    alive.add(civilization)  
def CivColour():
    r = rn.randint(0, 255)
    g = rn.randint(0, 255)
    b = rn.randint(0, 255)
    return (r, g, b)
class Civ(pygame.sprite.Sprite):
    def __init__(self, colour, centre, radius, tech):
        self.Owngroup = pygame.sprite.GroupSingle()
        self.tech = tech
        self.radius = radius
        self.colour = colour
        self.centre = centre
        pygame.sprite.Sprite.__init__(self)
        
    def Advance(self, Surface):
        self.tech += (1 - self.tech) * 0.01
        self.radius += self.tech
        self.rect = pygame.Rect(self.centre[0], self.centre[1], 2*self.radius, 2*self.radius)
        pygame.draw.circle(Surface, self.colour, self.centre, self.radius)
        if pygame.sprite.collide_circle(self, pygame.sprite.spritecollideany(self, alive)):
            Sprite = pygame.sprite.spritecollideany(self, alive)
            if Sprite.Owngroup != self.Owngroup:
                if Sprite.tech > self.tech:
                    pygame.draw.circle(Surface, "Black", self.centre, self.radius)
                    self.kill()
                if Sprite.tech < self.tech:
                    pygame.draw.circle(Surface, "Black", Sprite.centre, Sprite.radius)
                    Sprite.kill()
    


