# Name:- Arjun Chauhan
# Instagram Handle:- @rockstarjun.py

import turtle
t=turtle.Turtle()
win=turtle.Screen()
win.bgcolor("black")
t.speed(10)
def spiral(p):
    colours=["red","blue","green"]
    num=1
    while (num==True):
        t.pencolor(colours[p%3])
        t.pensize(3)
        t.forward(p)
        t.right(144)
        if p<=700:
            spiral(p+10)
            num+=1
        else:
            break
spiral(1)
turtle.done()