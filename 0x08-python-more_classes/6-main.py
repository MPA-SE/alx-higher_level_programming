#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

mon_rectangle_1 = Rectangle(2, 4)
mon_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del mon_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del mon_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
