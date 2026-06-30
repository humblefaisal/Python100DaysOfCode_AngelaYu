from turtle import Turtle
from constants import *

class Ball(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(stretch_len=BALL_SIZE_FACTOR,stretch_wid=BALL_SIZE_FACTOR)
        self.color(BALL_COLOR)
        self.penup()
        # default move right first
        self.x_vel = BALL_X_VELOCITY
        self.y_vel = 0
        self.x = 0
        self.y = 0
        self.update()
    
    def reset(self):
        self.x_vel = BALL_X_VELOCITY
        self.y_vel = 0
        self.x = 0
        self.y = 0
    def update(self):
        self.y+=self.y_vel / DELTA
        self.x+=self.x_vel / DELTA
        self.goto(self.x,self.y)
        # self.screen.ontimer(fun=self.update,t=(1000//REFRESH_RATE))
