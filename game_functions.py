import sys
import pygame
from pygame.sprite import Group
from Setting import settings
from ship import Ship
import game_functions as gf
from game_stats import Game_stats



def run_game():
    pygame.init()
    a = settings()
    screen = pygame.display.set_mode((a.screen_width,a.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #creat a ship
    ship = Ship(a,screen)
    
    #creat a group to save bullets 
    #Group() is a class from pygame.sprite 
    # bullets should out of while loop
    bullets = Group() 
    #creat a group of alien
    aliens = Group()
    gf.create_fleet(a,screen,aliens,ship)
    stats = Game_stats(a)
    while True:
        # monitor the event of keyboard and mouse
        gf.check_events(a,screen,ship,bullets)
        
        # to malke sure which parts are running
        if stats.game_active:
            ship.update()
            # the bullets are deleted 
            gf.update_bullets(a,screen,ship,aliens,bullets)
            gf.update_aliens(a,screen,ship,aliens,bullets,stats)
        gf.update_screen(a,screen,ship,bullets,aliens)
        
        
run_game()
