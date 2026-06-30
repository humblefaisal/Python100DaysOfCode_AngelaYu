import turtle
from D18Colors import colors
import random

if __name__=='__main__':
    t = turtle.Turtle()
    t.speed(10000)
    t.pensize(20)
    t.getscreen().bgcolor("black")
    w = t.getscreen().canvwidth
    h = t.getscreen().canvheight
    # turtle.hideturtle()
    t.penup()
    for i in range(0,2*h,70):
        t.goto(-w,i-h)
        for j in range(0,w,10):
            t.color(random.choice(colors))
            t.pendown()
            t.circle(10)
            t.penup()
            t.forward(70)
    turtle.done()
    screen = turtle.Screen()
    screen.exitonclick()
