#set a setting class to contain all of the settings in one module so 
# we do not have to add in settings in ohter places 
#but transfer a setting object

class settings():
    
    def __init__(self):
        #initialize the settings of the game
        #the setting of secreen all defualt settings
        self. screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (250, 250, 250)
        
        # settings of ship speed and the number of ships player can use
        self.ship_speed_factor = 2.5
        self.ship_limit = 3
        
        # settings of bullet speed and the number of bullets that can shoot if there is no bullet left
        self.bullet_speed_factor = 2
        self.bullet_allowed = 5
       
       # settings of alients speed and direction 
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
