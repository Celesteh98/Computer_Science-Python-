#Circle.py

from Shape2D import Shape2D

class Circle(Shape2D):
        def __init__(self,color = None, radius = None):
            super(Circle,self).__init__(color)
            self.radius =radius

        def getRadius(self):
            return self.radius

        def setRadius(self, radius):
            self.radius = radius

        def computeArea(self):
            return 3.14159 * (self.radius ** 2)

        def computePerimeter(self):
            return 3.14159 * (self.radius * 2)

        def getShapeProperties(self):
            return f"Shape: CIRCLE, Color: {self.color}, Radius: {self.radius}," \
            f" Area: {self.computeArea()}, Perimeter: {self.computePerimeter()}"
