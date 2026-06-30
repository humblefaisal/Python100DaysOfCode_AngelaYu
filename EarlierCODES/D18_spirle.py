import turtle
import math
pen = turtle.Turtle()
pen.pensize(2)

def draw_semi_circle(radius,right=True):
    pen.circle(radius,180)

toggle=True
rad=3
for i in range(1,50):
    rad*=1.2
    draw_semi_circle(rad,toggle)
    toggle=not toggle
turtle.done()