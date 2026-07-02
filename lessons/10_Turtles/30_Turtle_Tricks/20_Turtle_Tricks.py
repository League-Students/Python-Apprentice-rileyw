"""
# 20_Turtle_Tricks.py

In this assignment, you will use Tina the Turtle to draw a pentagon. 

- Each side of the pentagon should be a different color. 
- Use the turtle commands: tina.forward(), tina.left(), and tina.pencolor() to accomplish this.

Refer to the previous program, Meet_Tina.py, for examples of how to use turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

def tina.pentagon(color, length):
    tina.pencolor(color)
    tina.forward(length)
    tina.left(72)
# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()
tina.pentagon("blue", 50)
tina.pentagon("red", 50)
tina.pentagon("yellow", 50)
tina.pentagon("green", 50)
tina.pentagon("purple", 50)

turtle.exitonclick()                    # Close the window when we click on it