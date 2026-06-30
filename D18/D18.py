from turtle import Turtle,Screen,colormode,done
from colors import colors
import random
colormode(255)

def draw_square(tim,length=50):
    tim.forward(length)
    tim.right(90)
    tim.forward(length)
    tim.right(90)
    tim.forward(length)
    tim.right(90)
    tim.forward(length)
    return

def draw_dashed_line (tim:Turtle,length,stroke_length):
    travelled_distance = 0
    stroking = True
    while travelled_distance < length:
        if stroking :
            tim.pendown()
        else :
            tim.penup()
        tim.forward(min(stroke_length,length-travelled_distance))
        travelled_distance+=stroke_length
        stroking = not stroking
    return

def draw_polygon(tim:Turtle,length:int,num_sides:int):
    angle_rotation = 360.0 / num_sides
    curr_angle=0
    while curr_angle<360:
        tim.forward(length)
        tim.right(angle_rotation)
        curr_angle+=angle_rotation
    return

def draw_all_polygons(tim:Turtle,length):
    for i in range(3,11):
        tim.color(random.choice(colors))
        draw_polygon(tim,length,i)
    return

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
def random_walk(tim:Turtle,steps:int):
    dirs = [0,90,180,270] #rotate for directoin change
    SINGLE_WALK = 10
    for _ in range(steps):
        tim.color(random_color())
        tim.right(random.choice(dirs))
        tim.forward(SINGLE_WALK)
    return

def draw_spirograph(tim:Turtle = Turtle(),steps:int = 50,radius:int = 100):
    angle = 360.0/steps
    for _ in range(steps):
        tim.color(random_color())
        tim.circle(radius=radius)
        # tim.right(angle=angle)
        tim.setheading(tim.heading()+angle)
    return

tim = Turtle()
# tim.shape("turtle")
tim.speed(0)
# draw_square(tim=tim,length=100)
# draw_dashed_line(tim=tim,length=100,stroke_length=10)
# draw_all_polygons(tim=tim,length=50)
# random_walk(tim,100)
# draw_spirograph(tim,50,100)

# tim.goto(100,100)
# tim.teleport(-100,100)
# tim.onclick(
#     lambda x, y: draw_spirograph(tim, 50, 100)
# )
# done()

screen = Screen()
screen.exitonclick()