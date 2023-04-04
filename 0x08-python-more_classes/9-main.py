#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

mon_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(mon_square.area(), mon_square.perimeter()))
print(mon_square)
