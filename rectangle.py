from shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super(Rectangle, self).__init__()

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return self.height * 2 + self.width * 2
