import pygame
import random as rn
alive = pygame.sprite.Group()
CivColours = ["Purple", "Green", "Orange", "Teal", "Cyan", "Magenta", "Yellow", "White", "Blue", "Light Blue", "Red", "Pink"]
def spawnCiv(xy, NoOfCivs):
    print("Civilization number " + str(NoOfCivs) + " Spawned at " + str(xy))
    civilization = Civ(rn.choice(CivColours), xy, 10, 0.1)
    

    alive.add(civilization)      
class Civ(pygame.sprite.Sprite):
    def __init__(self, colour, centre, radius, tech):
        self.tech = tech
        self.radius = radius
        self.colour = colour
        self.centre = centre
        pygame.sprite.Sprite.__init__(self)
        
    def Advance(self):
        self.tech += (1 - self.tech) * 0.01
        self.radius += self.tech
        print(f"tech={self.tech:.6f}, radius={self.radius:.6f}")
        surface = pygame.display.get_surface()
        pygame.draw.circle(surface, self.colour, self.centre, self.radius)
    


