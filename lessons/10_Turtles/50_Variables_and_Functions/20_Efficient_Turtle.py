"""
# 20_Efficient_Turtle.py

In this program, use what you've learned about functions and variables to make a program that can draw a square, pentagon, and hexagon with a single function.

- Create a function that draws a polygon based on the number of sides passed to it as an argument.
- Use variables to calculate the angle needed to turn the turtle based on the number of sides.
- Call the function multiple times with different arguments to draw a square, pentagon, and hexagon.
"""

import turtle                            # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)             # Set the size of the window

tina = turtle.Turtle()                   # Create a turtle named tina

tina.shape('turtle')                     # Set the shape of the turtle to a turtle
tina.speed(2)                            # Move at a moderate speed, not too fast.

def draw_polygon(sides, size):

    angle = 360/sides
    
    for i in range(sides):
        tina.forward(size) 
        tina.left(angle)
draw_polygon(4, 50)                        # Draw a square

tina.penup()
tina.goto(-200, 200)                                      # Move tina to another spot on the screen
tina.pendown()
draw_polygon(5, 50)                        # Draw a pentagon

tina.penup()
tina.goto(-200, 0)
tina.pendown()
draw_polygon(6, 60)                        # Draw a hexagon

turtle.exitonclick()                     # Close the window when we click on it