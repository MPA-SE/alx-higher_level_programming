#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

mon_rectangle = Rectangle(2, 4)
print(str(mon_rectangle))
print("--")
print(mon_rectangle)
print("--")
print(repr(mon_rectangle))
print("--")
print(hex(id(mon_rectangle)))
print("--")

# create new instance based on representation
nouv_rectangle = eval(repr(mon_rectangle))
print(str(nouv_rectangle))
print("--")
print(nouv_rectangle)
print("--")
print(repr(nouv_rectangle))
print("--")
print(hex(id(nouv_rectangle)))
print("--")

print(nouv_rectangle is mon_rectangle)
print(type(nouv_rectangle) is type(mon_rectangle))
