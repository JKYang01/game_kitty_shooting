class Game_stats():
    # update the statistics in the game
    def __init__(self,a):
        self.a = a
        self.reset_stats()
        self.game_active = True
    def reset_stats(self):
        self.ship_left = self.a.ship_limit
