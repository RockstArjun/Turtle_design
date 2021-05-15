# Name:- Arjun Chauhan
# Instagram handle:- @rockstarjun

import turtle
t=turtle.Turtle()
win=turtle.Screen()
t.shape("classic")
win.bgcolor("black")
t.speed(2000)
t.penup()
t.setposition(-150,150)
t.pendown()
def spiral(p):
    colours=["dark blue","dark violet","grey"]
    num=1
    while (num==True):
        t.pencolor(colours[p%3])
        t.pensize(2)
        t.forward(p)
        t.right(122)
        if p>-600:
            spiral(p-5)
            num+=1
        else:
            break
spiral(350)

turtle.exitonclick()