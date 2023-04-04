#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

mon_rectangle_1 = Rectangle(8, 4)
print(mon_rectangle_1)
print("--")
mon_rectangle_1.print_symbol = "&"
print(mon_rectangle_1)
print("--")

mon_rectangle_2 = Rectangle(2, 1)
print(mon_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(mon_rectangle_2)
print("--")

mon_rectangle_3 = Rectangle(7, 3)
print(mon_rectangle_3)

print("--")

mon_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(mon_rectangle_3)

print("--")
