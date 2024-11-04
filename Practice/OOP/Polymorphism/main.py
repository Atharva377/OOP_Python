class Shape:
    def area(self):
        return f"The area of the fig"
        
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    
    def area(self):
        return 3.14*self.radius* self.radius
        
def print_area(shape):  # Use lowercase for instance variable
    shape_name = type(shape).__name__  # Get the name of the shape class
    print(f"The area of {shape_name} is {shape.area()}")
        
rectangle = Rectangle(4,5)
print_area(rectangle)
circle = Circle(7)
print_area(circle)