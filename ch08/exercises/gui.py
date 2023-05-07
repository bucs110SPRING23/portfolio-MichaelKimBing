class goombas:
    def __init__ (self):
        """
        Initializes the goombas or the moving obstacles
        """
        self.health = 1 
        self.hitbox = range(6)
        self.size  = 10
    
class mystery_box:
    def __init__(self):
        """
        Initializes the mystery box
        """
        self.hit = False
        self.touch = True
        self.height = (200,300)

class coins:
    def __init__(self, counter = 0):
        """
        Initializes counter for coin and after 100 then offers one extra life
        """
        self.counters = counter
        self.touch_coin = self.counters + 1 #there needs to be a controller 
        self.extra_lives = 1
        if self.touch_coin == 100:
            self.give = self.extra_lives + 1

class Tube:
    def __init__(self):
        """
        Initializes the tube transport
        """
        self.color = (200, 200, 250)
        self.position = (300, 300)
        self.access_tube = True


