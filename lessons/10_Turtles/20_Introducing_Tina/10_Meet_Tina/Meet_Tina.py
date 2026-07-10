import turtle
tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500, 500)
cam = 1
cam_colors = ["white", "blue", "red", "black", "green"]

def OpenCam1():
    if cam != 1
    print("Cam 1")
    screen.bgcolor(cam_colors[0])

def OpenCam2():
    print("Cam 2")
    screen.bgcolor(cam_colors[1])

screen.listen()
screen.onkey(OpenCam1, "1")
screen.onkey(OpenCam2, "2")


turtle.exitonclick()