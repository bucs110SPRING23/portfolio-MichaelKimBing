#Part A:
class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    
    def __str__(self):
        """
        Returning values for x coordinate,y coordinate, width, and height values
        """
        return f'(x:,{self.x}),(y:,{self.y}),width:{self.width},height:{self.height}'
                     


