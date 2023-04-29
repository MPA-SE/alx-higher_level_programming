#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

mon_rectangle_1 = Rectangle(8, 4)
mon_rectangle_2 = Rectangle(2, 3)

if mon_rectangle_1 is Rectangle.bigger_or_equal(mon_rectangle_1, mon_rectangle_2):
    print("mon_rectangle_1 is bigger or equal to mon_rectangle_2")
else:
    print("mon_rectangle_2 is bigger than mon_rectangle_1")


mon_rectangle_2.width = 10
mon_rectangle_2.height = 5
if mon_rectangle_1 is Rectangle.bigger_or_equal(mon_rectangle_1, mon_rectangle_2):
    print("mon_rectangle_1 is bigger or equal to mon_rectangle_2")
else:
    print("mon_rectangle_2 is bigger than mon_rectangle_1")
