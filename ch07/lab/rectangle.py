#Part A:
class Rectangle:
    def __init__(self, x, y, height, width):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(height)
        self.width = abs(width)
    
    def __str__(self):
        """
        Returning values for x coordinate,y coordinate, width, and height values
        args: (class) returns the values of the x,y,width, and height values
        return: (string) returns the values of the x,y,width, and height values in the format of (x:(x-coordinate)),(y:(y-coordinate)),width:(width value),height:(height value)
        """
        return f'(x:,{self.x}),(y:,{self.y}),width:{self.width},height:{self.height}'
                     


