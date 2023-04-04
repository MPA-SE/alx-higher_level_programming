#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

mon_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(mon_rectangle.area(), mon_rectangle.perimeter()))

del mon_rectangle

try:
    print(mon_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
