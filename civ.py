import pygame
import random as rn
import config
alive = pygame.sprite.Group()
def spawnCiv(xy):
    if rn.randint(0,100) <= config.ReadSetting(9):
        behaviour = True
    else:
        behaviour = False
    civilization = Civ(CivColour(), xy, 10, rn.randrange(1, 99900)/100000, 1000, behaviour)
    

    alive.add(civilization)  
def CivColour():
    r = rn.randint(0, 255)
    g = rn.randint(0, 255)
    b = rn.randint(0, 255)
    return (r, g, b)
class Civ(pygame.sprite.Sprite):
    def __init__(self, colour, centre, radius, tech, desperation, benevolent):
        self.Owngroup = pygame.sprite.Group()
        self.tech = tech
        self.radius = radius
        self.colour = colour
        self.centre = centre
        self.desperation = desperation
        self.benevolent = benevolent
        pygame.sprite.Sprite.__init__(self)
    
    def Victory(self):
        self.desperation =+ config.ReadSetting(12)
    def Combine(self, target):
        Group = self.Owngroup
        pygame.sprite.Group.add(Group, target)
        
        
        target.colour = self.colour
        print(str(self) + str(target) + "Combined")
    def Defeat(self):
        pygame.draw.circle(pygame.display.get_surface(), "Black", self.centre, self.radius)
        self.kill()

    def Advance(self):
        Surface = pygame.display.get_surface()
        self.tech += (1 - self.tech) * 0.01
        self.radius += self.tech
        self.desperation += (config.ReadSetting(11) / self.tech)
        self.rect = pygame.Rect(self.centre[0], self.centre[1], 2*self.radius, 2*self.radius)
        Desperate = False
        if self.desperation>1000:
            Desperate == True
        else:
            Desperate == False
        pygame.draw.circle(Surface, self.colour, self.centre, self.radius)
        if pygame.sprite.collide_circle(self, pygame.sprite.spritecollideany(self, alive)):
            Sprite = pygame.sprite.spritecollideany(self, alive)
            if Sprite.Owngroup != self.Owngroup:
                if not Desperate:
                    if not Sprite.desperation > 1000:
                        if self.benevolent:
                            if Sprite.benevolent:
                                self.Combine(Sprite)
                                self.Victory()
                                Sprite.Victory()
                            else:
                                if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                    self.Defeat()
                                    Sprite.Defeat()
                                if Sprite.tech > self.tech:
                                    self.Defeat()
                                    Sprite.Victory()
                                if Sprite.tech < self.tech:
                                    Sprite.Defeat()
                                    self.Victory()
                        if not self.benevolent:
                            if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                self.Defeat()
                                Sprite.Defeat()
                            if Sprite.tech > self.tech:
                                self.Defeat()
                                Sprite.Victory()
                            if Sprite.tech < self.tech:
                                Sprite.Defeat()
                                self.Victory()
                    else:
                        if self.benevolent:
                            if Sprite.benevolent:
                                self.Combine(Sprite)
                                self.Victory()
                                Sprite.Victory()
                            else:
                                if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                    self.Defeat()
                                    Sprite.Victory()
                                if Sprite.tech > self.tech:
                                    self.Defeat()
                                    Sprite.Victory()
                                if Sprite.tech < self.tech:
                                    self.Defeat()
                                    Sprite.Defeat()
                        if not self.benevolent:
                            if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                self.Defeat()
                                Sprite.Victory()
                            if Sprite.tech > self.tech:
                                self.Defeat()
                                Sprite.Victory()
                            if Sprite.tech < self.tech:
                                Sprite.Defeat()
                                self.Defeat()
                else:
                    if not Sprite.desperation > 1000:
                        if self.benevolent:
                            if Sprite.benevolent:
                                self.Combine(Sprite)
                                self.Victory()
                                Sprite.Victory()
                            else:
                                if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                    Sprite.Defeat()
                                    self.Victory()
                                if Sprite.tech > self.tech:
                                    self.Defeat()
                                    Sprite.Defeat()
                                if Sprite.tech < self.tech:
                                    Sprite.Defeat()
                                    self.Victory()
                        if not self.benevolent:
                            if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                self.Victory()
                                Sprite.Defeat()
                            if Sprite.tech > self.tech:
                                self.Defeat()
                                Sprite.Defeat()
                            if Sprite.tech < self.tech:
                                Sprite.Defeat()
                                self.Victory()
                    else:
                        if self.benevolent:
                            if Sprite.benevolent:
                                self.Combine(Sprite)
                                self.Victory()
                                Sprite.Victory()
                            else:
                                if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                    self.Defeat()
                                    Sprite.Defeat()
                                if Sprite.tech > self.tech:
                                    self.Defeat()
                                    Sprite.Victory()
                                if Sprite.tech < self.tech:
                                    Sprite.Defeat()
                                    self.Victory()
                        if not self.benevolent:
                            if Sprite.tech - self.tech * 1 < config.ReadSetting(10)/100:
                                self.Defeat()
                                Sprite.Defeat()
                            if Sprite.tech > self.tech:
                                self.Defeat()
                                Sprite.Victory()
                            if Sprite.tech < self.tech:
                                Sprite.Defeat()
                                self.Victory()


                    


                    
    


