#testFile.py

from Square import Square
from Circle import Circle

class TestCircle:
    def setup(self):
        self.X = Circle("orange", 4)
        self.Y = Circle("green", 8)

    def testgetRadius(self):
        assert self.X.getRadius() == 4
        assert self.Y.getRadius() == 8

    def testsetRadius(self):
        self.X.setRadius(50)
        assert self.X.radius == 50
        self.Y.setRadius(100)
        assert self.Y.radius == 100

    def testcomputeself(self):
        assert self.X.computeArea() == (3.14159 * (4 **2))
        assert self.Y.computeArea() == (3.14159 * (8 **2))

    def testcomputerPerimeter(self):
        assert self.X.computePerimeter() == (3.14159 * 4 * 2)
        assert self.Y.computePerimeter() == (3.14159 * 8 * 2)

    def testgetShapeProperties(self):
        assert self.X.getShapeProperties() == f"Shape: CIRCLE, color: {self.X.color}, Radius: {self.X.radius},"'\n'
        f"Area: {self.X.computeArea()}, Perimeter: {self.X.computePerimeter()}"

        assert self.Y.getShapeProperties() == f"Shape: CIRCLE, color: {self.Y.color}, Radius: {self.Y.radius},"'\n'
        f"Area: {self.Y.computeArea()}, Perimeter: {self.Y.computePerimeter()}"

    def testsetColor(self):
        self.X.setColor("blue")
        assert self.X.color == "blue"

    def testgetColor(self):
        assert self.X.getColor() == "orange"

class TestSquare:
    def setup(self):
        self.X = Square("orange", 4)
        self.Y = Square("green", 8)

    def testgetRadius(self):
        assert self.X.getSide() == 4
        assert self.Y.getSide() == 8

    def testsetRadius(self):
        self.X.setSide(50)
        assert self.X.side == 50
        self.Y.setSide(100)
        assert self.Y.side == 100

    def testcomputeself(self):
        assert self.X.computeArea() == (4 **2)
        assert self.Y.computeArea() == (8 **2)

    def testcomputerPerimeter(self):
        assert self.X.computePerimeter() == (4 * 2)
        assert self.Y.computePerimeter() == (8 * 2)

    def testgetShapeProperties(self):
        assert self.X.getShapeProperties() == f"Shape: SQUARE, color: {self.X.color}, Side: {self.X.side},"'\n'
        f"Area: {self.X.computeArea()}, Perimeter: {self.X.computePerimeter()}"

        assert self.X.getShapeProperties() == f"Shape: SQUARE, color: {self.Y.color}, Side: {self.Y.side},"'\n'
        f"Area: {self.Y.computeArea()}, Perimeter: {self.Y.computePerimeter()}"

    def testsetColor(self):
        self.X.setColor("blue")
        assert self.X.color == "blue"

    def testgetColor(self):
        assert self.X.getColor() == "orange"

class testShape2D:
    def setup(self):
        self.X = Shape2D("yellow")

    def testsetColor(self):
        self.X.setColor("blue")
        assert self.X.Color() == "blue"

    def testgetColor(self):
        assert self.X.getColor() == "blue"

    def testgetShapeProperties(self):
        assert self.X.getShapeProperties() == f"Shape: N/A, Color: {self.X.color}"

  
