"""
# 30_Pentagon_Crazy.py

This program already works. Run it, then change it to make it draw a different pattern.

uid: QG1OFNKY
name: Pentagon Crazy
"""

import random
import turtle

colors = ("pink", "cyan", "lime", "yellow", "orange")

def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def get_next_color(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600, startx=0, starty=0)

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)
my_turtle.width(1)

sides = 5
angle = 360 / sides

for i in range(1000000):
    my_turtle.width(i/100+1)
    my_turtle.pencolor(get_next_color(i))
    my_turtle.forward(i)
    my_turtle.right(angle + 1)
