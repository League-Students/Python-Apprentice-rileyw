import turtle
tina = turtle.Turtle()
tina.shape = ("turtle")
screen = turtle.Screen()
screen.setup(500, 500)
cam = 1
cam_colors = ["white", "blue", "red", "black", "green", "gray"]

def OpenCam1():
    if cam != 1:
        print("Cam 1")
        cam = 1
    screen.bgcolor(cam_colors[0])

def OpenCam2():
    if cam != 2:
        print("Cam 2")
        cam = 2
    screen.bgcolor(cam_colors[1])

def OpenCam3():
    if cam != 3:
        print("Cam 3")
        cam = 3
    screen.bgcolor(cam_colors[2])

def OpenCam4():
    if cam != 4:
        print("Cam 4")
        cam = 4
    screen.bgcolor(cam_colors[3])

def OpenCam5():
    if cam != 5:
        print("Cam 5")
        cam = 5
    screen.bgcolor(cam_colors[4])

def OpenOffice():
    if cam != 6:
        print("Office")
        cam = 6
    screen.bgcolor(cam_colors[5])

screen.listen()
screen.onkey(OpenCam1, "1")
screen.onkey(OpenCam2, "2")
screen.onkey(OpenCam3, "3")
screen.onkey(OpenCam4, "4")
screen.onkey(OpenCam5, "5")
screen.onkey(OpenOffice, "s")


turtle.exitonclick()