# game_kitty_shooting
A simple game by employing pygame packages 
## Different parts of this project
This simple game have four parts including the classes of characaters and characters' settings
the class of opporational functions , the class of game status and the class of invasion 
### The fuctions 
#### Monitor the action of keyboards
```ruby
def check_events(a,screen,ship,bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        # the react of the opporation of keys 
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event,a,screen,ship,bullets)
        # then add in class ship as a prameter of check_event
        # in alien_invation.py
        # when the player does not press the key    
        elif event.type == pg.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,a,screen,ship,bullets):
    # react of press key
    if event.key == pg.K_RIGHT:
        ship.moving_right =True
    elif event.key == pg.K_LEFT:
        ship.moving_left =True
    elif event.key == pg.K_SPACE:
        fire_bullet(a,screen,ship,bullets)
def check_keyup_events(event,ship):
    # react of lose key
    if event.key == pg.K_RIGHT:
        ship.moving_right =False
    elif event.key == pg.K_LEFT:
        ship.moving_left= False
```
#### Display the game
``` ruby
def update_screen(a, screen, ship,bullets,aliens):
    # update the image on the screen and change to the new screen
    # redraw the screen in every loop
    screen.fill(a.bg_color)
    # redraw bullets after ship and alients
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #show the recent screen
    pg.display.flip()
```
#### The action of bullets
``` ruby
def fire_bullet(a,screen,ship,bullets):
    # this function is called when pressing the space key
    if len(bullets)< a.bullet_allowed:
        new_bullet = Bullet(a,screen,ship)
        bullets.add(new_bullet) # equales to Group.add(new_bullet)     
# self.move_right self.move_left are defined in class ship 
# as moving signal at the begining they are both = False 

def update_bullets(a,screen,aliens,ship,bullets):
    # the function update is definded in class bullet
    bullets.update()
    #delete the bullet that disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(a,screen,aliens,ship,bullets)
    
``` 
#### Fuctions of creating aliens
``` ruby
def get_number_alien_x(a,alien_width):
    # creat an alien and caculate how many aliens can stand in one row
    available_space_x = a.screen_width - 2 * alien_width
    # use init to make sure it is a integer
    number_alien_x = int(available_space_x/ (2 * alien_width))
    return number_alien_x
    
def get_number_row(a,ship_height,alien_height):
    available_space_y = a.screen_height -2* alien_height - ship_height
    number_row = int(available_space_y/(2 * alien_height))
    return number_row
```
#### Function of checking the collisions among ship, aliens and bullets 
``` ruby
def check_bullet_alien_collisions(a,screen,ship,aliens,bullets):
    # if bullet hit alien delet the bullet and alien
    collisions = pg.sprite.groupcollide(bullets,aliens, True, True)
    # if aliens are killed off delete the bullet and creat new fleet of alien     
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(a,screen,aliens,ship)
def ship_hit(a,screen,ship,aliens,bullets,stats):
    # react the ship crushed by alients
    # ship_left -1
    if stats.ship_left > 0:
        stats.ship_left -= 1
    # clear alient and the bullet list
        aliens.empty()
        bullets.empty()
        create_fleet(a,screen,aliens,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False

``` 

#### The actions of aliens
``` ruby
def creat_alien(a,screen,aliens,alien_number,row_number):
     alien = Alien(a,screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2 * alien_width * alien_number
     alien.rect.x = alien.x
     alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
     aliens.add(alien)

def create_fleet(a,screen,aliens,ship):
    # the spacing is alien's width
    alien = Alien(a,screen)
    # creat an alien adn calculate the number of aliens in one row
    number_alien_x = get_number_alien_x(a,alien.rect.width)
    number_row = get_number_row(a,alien.rect.height, ship.rect.height)
    # the first line of aliens
    for row_number in range(number_row):
        for alien_number in range (number_alien_x):
            creat_alien(a,screen,aliens,alien_number,row_number)
        
def check_fleet_edges(a,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(a,aliens)
            break

def change_fleet_direction(a,aliens):
    for alien in aliens.sprites():
        alien.rect.y += a.fleet_drop_speed
    a.fleet_direction *= -1
        
def check_aliens_bottom(a,screen,ship,aliens,bulltes,stats):
    #check if there are aliens reach the bottom
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(a,screen,ship,aliens,bullets,stats)
            break 
            
def update_aliens(a,screen,ship,aliens,bullets,stats):
    check_fleet_edges(a,aliens)
    aliens.update()
    
    if pg.sprite.spritecollideany(ship,aliens):
        ship_hit(a,screen,ship,aliens,bullets,stats)
        
    check_aliens_bottom(a,screen,ship,aliens,bullets,stats) 
```
