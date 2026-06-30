from turtle import Turtle,done
import turtle
from random import *
import time
from D18Colors import explosion_colors as colors
import threading
rocket_shape = ((0, 0), (10, 30), (20, 0), (10, -40))  # rough rocket shape
turtle.register_shape("rocket", rocket_shape)
PEN_SIZE=5
t=Turtle()
ROOT = t.getscreen().getcanvas().winfo_toplevel()
WIDTH = ROOT.winfo_width()
HEIGHT = ROOT.winfo_height()
INITIAL_VELOCITY=30
EXPLOSION_LAYERS=4
gens:list = []

def move_spark(pos,angle,vanish_length=200):
    v=INITIAL_VELOCITY*0.5
    t=Turtle()
    setup_turtle(t,pos,angle)
    t.stamp()
    len_travel=0
    while len_travel<=vanish_length:
        yield 0
        wid,len,temp=t.shapesize()
        t.shapesize(stretch_wid=wid*0.9,stretch_len=len*0.9)
        t.forward(v)
        len_travel+=v
        t.clearstamps()
        t.stamp()
        v*=0.95
    t.clearstamps()

def setup_turtle(t:Turtle,pos:tuple,angle):
    t.speed(1)
    t.hideturtle()
    t.shape("circle")
    t.penup()
    t.pensize(PEN_SIZE)
    t.teleport(pos[0],pos[1])
    t.left(angle)
    t.color(choice(colors))
def launch_rocket():
    t=Turtle()
    x=randint(0,WIDTH)
    x-=WIDTH/2
    y=-HEIGHT/2
    setup_turtle(t,(x,y),90)
    t.shape("rocket")
    velocity=INITIAL_VELOCITY
    curr_id=t.stamp()
    while y <= HEIGHT*0.15:
        yield 0
        prev_id=curr_id
        t.clearstamps()
        t.stamp()
        velocity*=0.95
        t.forward(velocity)
        y+=velocity
    t.clearstamps()
    for layer in range(EXPLOSION_LAYERS):
        yield 0
        particles_in_layer = randint(3,5)
        for particle in range(particles_in_layer):
            angle = randint(0,180)
            gen1 = move_spark((x,y),angle)
            gen2 = move_spark((x,y),angle+180)
            gens.extend([gen1,gen2])

def generator_runner(gens):
    screen=t.getscreen()
    screen.tracer(0)
    rocket:int=1
    particles_rem=0
    while len(gens)>0:
        rem_gen=[]
        for gen in gens[:]:
            try:
                next(gen)
            except StopIteration:
                rem_gen.append(gen)
                pass
        for r in rem_gen:
            gens.remove(r)
            particles_rem+=1
        rocket=max(rocket-particles_rem//32,0)
        particles_rem%=32
        screen.update()
        prob=randint(0,7)
        if prob%7==0 and rocket<4:
            rocket+=1
            gens.append(launch_rocket())
        print(len(gens))

gens.append(launch_rocket())
generator_runner(gens)
done()