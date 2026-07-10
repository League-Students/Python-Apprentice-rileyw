import turtle
tina = turtle.Turtle()
tina.shape("turtle")
screen = turtle.Screen()
screen.setup(500, 500)
cam = 1
cam_colors = ["white", "blue", "red", "black", "green", "gray"]
tina_cam = [1, 3, 4, 5]
tina_progress = 0

def ShowHideTina(cam_num):
    if cam_num == tina_cam[tina_progress]:
        tina.showturtle()
    else:
        tina.hideturtle()
def OpenCam1():
    ShowHideTina(1)
    print("Cam 1")
    screen.bgcolor(cam_colors[0])

def OpenCam2():
    ShowHideTina(2)
    print("Cam 2")
    screen.bgcolor(cam_colors[1])

def OpenCam3():
    ShowHideTina(3)
    print("Cam 3")
    screen.bgcolor(cam_colors[2])

def OpenCam4():
    ShowHideTina(4)
    print("Cam 4")
    screen.bgcolor(cam_colors[3])

def OpenCam5():
    ShowHideTina(5)
    print("Cam 5")
    screen.bgcolor(cam_colors[4])

def OpenOffice():
    ShowHideTina(0)
    print("Office")
    screen.bgcolor(cam_colors[5])

OpenOffice()

screen.listen()
screen.onkey(OpenCam1, "1")
screen.onkey(OpenCam2, "2")
screen.onkey(OpenCam3, "3")
screen.onkey(OpenCam4, "4")
screen.onkey(OpenCam5, "5")
screen.onkey(OpenOffice, "s")


turtle.exitonclick()