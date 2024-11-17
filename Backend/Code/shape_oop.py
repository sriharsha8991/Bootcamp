class Shape:
    def __init__(self,name) :
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def area(self):
        raise NotImplementedError("Subclasses should have this function")
    
    def display_info(self):
        print(f"{self.get_name()} and Area is: {self.area()}")

import math  
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    
class Rectangle(Shape):
    def __init__(self, length,width):
       super().__init__("Rectangle")
       self.length = length
       self.width = width

    def area(self):
        return self.width * self.length
    

circle = Circle(5)
circle.display_info()
