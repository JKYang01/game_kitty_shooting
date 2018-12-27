import pygame as pg

class Ship():
    
    def __init__(self, a, screen):
        # initialize the position of the ship
        self.screen = screen
        self.a = a  # a is factors in class setting() 
        # load the image of the ship and the rectangle
        image1 = pg.image.load('image/alient.bmp')
        # design the size of the image when it is too big or small
        # use function: pygame.transform.scale(name,(width, height))
        self.image = pg.transform. scale(image1,(90,80))
        # image2 = pg.transform.rotozoom(image1,0,2) means:
        # rotate by 0 degree and multiply size by 2
        
        # use function get_rect() to get the attributes of the surface
        # and deal with the images as rectangels  set the x,y coordination of the center of the rectangle
        # receive the image rectangular in self.rect
        self.rect = self.image.get_rect() 
        
        # receive the screen rectangular in self_screen_rect
        self.screen_rect = screen.get_rect()

        # put every new ship at the bottom 
        # put the image at the center of x axil of the screen
        self.rect.centerx = self.screen_rect.centerx
        # put the image at the bottome of secreen 
        self.rect.bottom = self.screen_rect.bottom
        # save the xiaoshu in the center attribution use cunction .float()
        self.center = float(self.rect.centerx)
        
        #the signal of moving
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # modify the position of the ship according to the signal
        # the position of image is self.rect 
        # the scale of screen is self.screen_rect 
        # the position of image should within the screen scale
        # use if to define if the position is over the screen scale 
        # it will stop by the edge 
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.center += self.a.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.a.ship_speed_factor
        
        # update the object of rect depend on self.center
        self.rect.centerx = self.center
        
    def blitme (self):
        # draww the ship in selected positon use function .bulit()
        # draw the images on position with the attributs
        # which is assigned by and self.image self.rect
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        self.center = self.screen_rect.centerx

