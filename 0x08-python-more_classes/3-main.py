#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

mon_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(mon_rectangle.area(), mon_rectangle.perimeter()))

print(str(mon_rectangle))
print(repr(mon_rectangle))

print("--")

mon_rectangle.width = 10
mon_rectangle.height = 3
print(mon_rectangle)
print(repr(mon_rectangle))
