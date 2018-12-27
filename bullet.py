import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    # manage the factor of bullets
    
    def __init__(self, a, screen, ship):
    # at the position of the ship, react an object of bullet
        super(Bullet, self).__init__()
        self.screen = screen
        
        # creat a regtangle at the coordination (0,0), 
        # then set the correct position use fuction .Rect()
        # the parameters of bullet have set in classs setting
        image1 = pg.image.load('image/ship.bmp')
        self.image = pg.transform.scale(image1,(30,30))
        self.rect = self.image.get_rect() # creat a regtangle of bullet 
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #save the position of bullet useing .float()
        self.y = float(self.rect.y)
        self.speed_factor = a.bullet_speed_factor
    
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        #pg.draw.rect(self.screen, self.rect)
        self.screen.blit(self.image, self.rect)
