from rectangle import Rectangle
from square import Square

_rectangle = Rectangle(5, 6)
_square = Square(5)

print "rectangle"
print ("perimeter " + str(_rectangle.perimeter()))
print ("area " + str(_rectangle.area()))
print "------------------"
print "square"
print ("perimeter " + str(_square.perimeter()))
print ("area " + str(_square.area()))
print "------------------"
