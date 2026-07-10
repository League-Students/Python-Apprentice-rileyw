import turtle
tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500, 500)

cam_colors = ["white", "blue", "red", "black", "green"]

def OpenCam(number):
    print ("Cam 1")
    screen.bgcolor(cam_colors[number - 1])

screen.listen()
screen.onkey(OpenCam(1), 1)