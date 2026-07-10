import turtle
import time
tina = turtle.Turtle()
tina.shape("turtle")
screen = turtle.Screen()
screen.setup(500, 500)
cam = 0
cam_colors = ["white", "blue", "red", "black", "green", "gray"]
tina_cam = [1, 3, 4, 5, 6]
tina_progress = 0
def move_tina():
    global tina_progress
    tina_progress += 1
    ShowHideTina()
    screen.ontimer(move_tina, 5000)
if tina_cam[tina_progress] == 6
    print("JUMPSCARE")
    

def ShowHideTina():
    global cam
    if cam == tina_cam[tina_progress]:
        tina.showturtle()
    else:
        tina.hideturtle()
def OpenCam1():
    global cam
    cam = 1
    ShowHideTina()
    screen.bgcolor(cam_colors[0])

def OpenCam2():
    global cam
    cam = 2
    ShowHideTina()
    screen.bgcolor(cam_colors[1])

def OpenCam3():
    global cam
    cam = 3
    ShowHideTina()
    screen.bgcolor(cam_colors[2])

def OpenCam4():
    global cam
    cam = 4
    ShowHideTina()
    screen.bgcolor(cam_colors[3])

def OpenCam5():
    global cam
    cam = 5
    ShowHideTina()
    screen.bgcolor(cam_colors[4])

def OpenOffice():
    global cam
    cam = 0
    screen.bgcolor(cam_colors[5])

OpenOffice()

screen.listen()
screen.onkey(OpenCam1, "1")
screen.onkey(OpenCam2, "2")
screen.onkey(OpenCam3, "3")
screen.onkey(OpenCam4, "4")
screen.onkey(OpenCam5, "5")
screen.onkey(OpenOffice, "s")

screen.ontimer(move_tina, 5000)

turtle.exitonclick()