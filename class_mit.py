

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sqaure(self):
        x_square = self.x **2
        y_square = self.y **2 
        return (x_square, y_square)
    
    def square_root(self):
        x_square = self.x **2
        y_square = self.y **2 
        sqrt = x_square**0.5 + y_square**0.5
        return sqrt
    
    def distance(self, other):
        x_dis = (self.x - other.x)**2
        y_dis = (self.y - other.y)**2 
        dist = (x_dis + y_dis)**0.5
        return dist
    
    def __str__(self):
        return f"<{self.x},{self.y}>"
    
    def __add__(self,other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        # return (sum_x + sum_y)
        return Coordinate(self.x + other.x,  self.y + other.y)
    
    def __len__(self):
        return 1
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    
    def __eq__(self, other):
        # First make sure `other` is of the same type 
        assert type(other) == type(self)
        # Since `other` is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'


c = Coordinate(3,2)
o = Coordinate(0,0)
print(c)
print(c.sqaure())
print(c.square_root())
print(Coordinate.distance(c,o))
print(isinstance(c,Coordinate))
print("Add", c + o)
print(len(c))
print(c.__len__())
print(repr(c))