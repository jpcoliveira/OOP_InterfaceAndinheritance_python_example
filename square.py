from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
        super(Square, self).__init__(side_length, side_length)
