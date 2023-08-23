from turtle import *
import turtle
import random

setup(width=500, height=500)

def background():

    screen = turtle.Screen() 

    color = (random.random(), random.random(), random.random())
    
    screen.bgcolor(color)

    t = turtle.Turtle()

    t.speed(10000)

    for i in range(100):
       draw_circle(t)

    t.hideturtle()


def draw_circle(t):
    pen_color = (random.random(), random.random(), random.random())
    fill_color = (random.random(), random.random(), random.random())
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.pensize(random.randint(1, 10))
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    radius = random.randint(10, 50)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def move_turtle(x, y):
    penup()
    goto(x, y)
    pendown()


def head():
    # face
    move_turtle(-40, 90)
    fillcolor("tan")
    begin_fill()
    seth(270)
    forward(10)
    for i in range(4):
        circle(30, 90)
        forward(18)
    seth(90)
    forward(5)
    circle(5, 220)
    forward(20)
    end_fill()
    move_turtle(37, 85)
    fillcolor("tan")
    begin_fill()
    seth(90)
    for j in range(20):
        forward(1)
        right(11)
    forward(19)
    end_fill()

    # hair
    move_turtle(37, 82)
    fillcolor("black")
    begin_fill()
    seth(90)
    forward(20)
    backward(10)
    seth(30)
    forward(4)
    seth(90)
    forward(19)
    for a in range(120, 280, 10):
        forward(7.8)
        seth(a)
    forward(10)
    seth(285)
    forward(10)
    seth(350)
    forward(1)
    seth(88)
    forward(20)
    seth(57)
    forward(18)
    seth(270)
    circle(15, 90)
    for k in range(2):
        seth(80)
        forward(15)
        seth(270)
        circle(15, 90)
    seth(80)
    forward(19)
    seth(320)
    forward(11)
    for b in range(16):
        right(3)
        forward(1)
    forward(10)
    seth(0)
    forward(4)
    end_fill()

    # left eye
    move_turtle(-10, 80)
    fillcolor("")
    begin_fill()
    forward(4)
    circle(2, 90)
    forward(18)
    seth(180)
    forward(27)
    seth(270)
    forward(15)
    circle(4, 90)
    forward(27)
    end_fill()

    # right eye
    move_turtle(20, 80)
    fillcolor("")
    begin_fill()
    forward(5)
    circle(4, 90)
    forward(16)
    seth(180)
    forward(27)
    seth(270)
    forward(18)
    circle(2, 90)
    forward(16)
    end_fill()
    move_turtle(-40, 90)
    forward(10)
    move_turtle(-4, 90)
    forward(7)
    move_turtle(30, 90)
    forward(9)

    def innereye():
        fillcolor("black")
        begin_fill()
        seth(270)
        for e in range(2):
            circle(2, 180)
            forward(2)
        end_fill()

    move_turtle(-12, 90)
    innereye()

    move_turtle(5, 90)
    innereye()

    # nose
    seth(0)
    move_turtle(0, 76)
    fillcolor("")
    begin_fill()
    circle(4, 340)
    end_fill()

    # smile
    move_turtle(-23, 72)
    seth(260)
    fillcolor("red")
    pencolor("black")
    pensize(1)
    begin_fill()
    circle(3, 10)

    for n in range(60):
        forward(0.5)
        left(2.5)
        if n > 30 and n < 40:
            right(0.1)
            forward(2.5)
            left(1.5)

    end_fill()


def body():
    #bow tie
    move_turtle(0, 42)
    fillcolor("black")
    pencolor("black")
    begin_fill()
    seth(30)
    forward(20)
    seth(180)
    forward(37)
    seth(330)
    forward(22)
    end_fill()

    # Cloths
    # skyblue
    move_turtle(22, 33)
    fillcolor("skyblue")
    begin_fill()
    seth(270)
    forward(36)
    seth(180)
    forward(50)
    seth(90)
    forward(36)
    backward(40)
    seth(180)
    forward(10)
    seth(90)
    forward(21)
    for i in range(10):
        forward(2)
        right(1.4)
    seth(35)
    forward(18)
    move_turtle(15, 40)
    move_turtle(22, 42)
    seth(320)
    forward(7)
    seth(300)
    for j in range(42):
        forward(0.5)
        right(0.5)
        if j > 30 and j < 35:
            forward(1.5)
            right(0.1)
        elif j > 36:
            forward(3)
            left(0.6)

    forward(2)
    seth(185)
    forward(18)
    seth(90)
    forward(40)
    end_fill()

    # right hands
    move_turtle(22, -1)
    fillcolor("tan")
    begin_fill()
    seth(270)
    forward(30)
    circle(4, 180)
    forward(10)
    backward(13)
    seth(0)
    circle(10, 100)
    for h in range(10):
        forward(1.9)
        left(1)
    seth(180)
    forward(12)
    end_fill()
    move_turtle(-28, -7)
    # left hand
    fillcolor("tan")
    begin_fill()
    seth(180)
    forward(7)
    circle(14, 180)
    seth(90)
    forward(15)
    backward(15)
    seth(0)
    circle(5, 90)
    seth(90)
    forward(25)
    end_fill()


def legs():
    # legs
    move_turtle(-25, -32)
    fillcolor("tan")
    begin_fill()
    seth(267)
    forward(35)
    seth(0)
    forward(23)
    seth(87)
    forward(33)
    seth(180)
    forward(23)
    backward(47)
    seth(277)
    forward(34)
    seth(180)
    forward(22)
    seth(95)
    forward(35)
    end_fill()

    # Socks
    move_turtle(-27, -68)
    fillcolor("ivory")
    begin_fill()
    seth(268)
    forward(23)
    seth(0)
    forward(25)
    seth(90)
    forward(24)
    seth(180)
    forward(24)
    end_fill()

    move_turtle(8, -68)
    fillcolor("ivory")
    begin_fill()
    seth(0)
    forward(18)
    seth(272)
    forward(23)
    seth(180)
    forward(22)
    seth(95)
    forward(25)
    end_fill()

    # shorts
    move_turtle(-27, -2)
    fillcolor("darkblue")
    begin_fill()
    seth(0)
    forward(50)
    seth(270)
    forward(35)
    seth(180)
    forward(22)
    seth(100)
    forward(10)
    seth(260)
    forward(10)
    seth(180)
    forward(25)
    seth(90)
    forward(32)
    end_fill()


def shoes():
    move_turtle(9, -90)
    fillcolor("skyblue")
    begin_fill()
    seth(180)
    circle(10, 180)
    forward(40)
    circle(3, 120)
    seth(150)
    forward(29)
    seth(180)
    forward(25)
    end_fill()

    move_turtle(0, -90)
    fillcolor("skyblue")
    begin_fill()
    forward(30)
    seth(212)
    forward(17)
    circle(7, 100)
    seth(0)
    forward(42)
    seth(90) 
    forward(22)
    end_fill()


def cartoondetails():
    pensize(0)
    def rectangle():
        seth(180)
        forward(50)
        seth(270)
        forward(3)
        seth(0)
        forward(50)
        seth(90)
        forward(3)
    # shirt detail
    move_turtle(22, 26)
    fillcolor("red")
    begin_fill()
    rectangle()
    end_fill()

    move_turtle(22, 22)
    fillcolor("yellow")
    begin_fill()
    rectangle()
    end_fill()

    move_turtle(14, 42)
    fillcolor("ivory")
    pencolor("black")
    shape("triangle")
    seth(299)
    stamp()

    move_turtle(-15, 42)
    fillcolor("ivory")
    pencolor("black")
    shape("triangle")
    seth(245)
    stamp()
    turtle.exitonclick()


def main():
    background()
    body()
    legs()
    shoes()
    head()
    cartoondetails()


main()
