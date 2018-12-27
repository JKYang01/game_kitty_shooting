import pygame as pg

from pygame.sprite import Sprite

class Alien(Sprite):
    
    def __init__(self, a, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.a = a
        image1 = pg.image.load('image/alient5.bmp')
        self.image = pg.transform.scale(image1,(90,60))
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y =self.rect.height
        self.x = float(self.rect.x)
        
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
    
    def update(self):
        self.x += (self.a.alien_speed_factor * self.a.fleet_direction)
        self.rect.x = self.x
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
