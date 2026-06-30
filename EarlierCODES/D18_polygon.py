import turtle
from D18Colors import colors
from random import choice
def draw_polygon(t:turtle.Turtle,side_length,side_num):
    # t.begin_fill()
    angle = 360.0/side_num
    for _ in range(0,side_num):
        t.forward(side_length)
        t.left(angle)
    for _ in range(0,side_num):
        t.forward(side_length)
        t.right(angle)
    # while True:
    #     t.forward(200)
    #     t.left(170)
    #     if abs(t.pos()) < 1:
    #         break
    # t.end_fill()
t = turtle.Turtle()
t.color("red")
t.fillcolor("yellow")
t.pensize(2)
for i in range(3,11):
    t.color(choice(colors))
    draw_polygon(t,100,i)
turtle.done()

# import turtle as t
# from random import random

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)