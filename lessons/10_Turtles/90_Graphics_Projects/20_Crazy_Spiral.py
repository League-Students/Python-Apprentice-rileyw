"""
# 20_Crazy_Spiral.py

Make your own crazy spiral with a pattern like
in 10_Flaming_Ninja_Star.py, but use what you've learned about loops

uid: zfzMbyH7
name: Crazy Spiral
"""
import turtle
import random
t = turtle.Turtle()
turtle.setup(600, 600, 0, 0)            # Set the size of the window
window = turtle.Screen()
left = 90
forward = 2
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))
while True:
    t.left(left)
    t.forward(forward)
    forward = forward + 2
    left = left - 1
    t.pencolor(get_random_color())

