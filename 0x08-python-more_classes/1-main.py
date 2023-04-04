#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

mon_rectangle = Rectangle(2, 4)
print(mon_rectangle.__dict__)

mon_rectangle.width = 10
mon_rectangle.height = 3
print(mon_rectangle.__dict__)
