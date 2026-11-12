# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if type(width) != int or type(height) != int:
            raise TypeError("Width and height must be integers")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")

        self.width = width
        self.height = height

    def is_square(self):
        return self.width == self.height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    