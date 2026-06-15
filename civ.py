import pygame
alive = pygame.sprite.Group()
def spawnCiv(xy, NoOfCivs):
    print("Civilization number " + str(NoOfCivs) + " Spawned at " + str(xy))
    civilization = Civ("purple", 20 ,20, xy)
    

    alive.add(civilization)

    pygame.display.flip()

def handleCiv(screen):
    alive.update()    
    alive.draw(screen) 
    pygame.display.flip()       


class Civ(pygame.sprite.Sprite):
    def __init__(self, colour, height, width, centre):
        super().__init__()

        self.image = pygame.Surface([width, height])

        pygame.draw.circle(self.image, colour, centre, width)