from turtle import Turtle
import math
from constants import *
def convert_to_int(nums:float):
    x = round(nums[0]/SQUARE_SIZE) * SQUARE_SIZE
    y = round(nums[1]/SQUARE_SIZE) * SQUARE_SIZE
    return (x,y)
class Snake :
    def __init__(self,screen):
        self.screen = screen
        self.tims = [Turtle(shape="square"),Turtle(shape="square"),Turtle(shape="square")]
        self.snake_curr_size:int = 3
        self.heading = 0
        self.speed=START_SNAKE_SPEED  #movement in second 
        self.last_pos = None
        for index,tim in enumerate(self.tims):
            tim.color("green")
            tim.penup()
            tim.teleport(STARTING_COORDINATE[0]-index*SQUARE_SIZE,STARTING_COORDINATE[1])
        self.screen.update()
    
    def move_forward(self):
        self.tims[0].setheading(self.heading)
        prev = self.tims[0].pos()
        self.tims[0].forward(SQUARE_SIZE)
        length = len(self.tims)
        for idx in range(1,length):
            curr = self.tims[idx].pos()
            self.tims[idx].teleport(prev[0],prev[1])
            prev = curr
        self.last_pos = prev
        self.update()  
    
    def update(self):
        self.screen.update()
    
    def rotate(self,angle):
        """angle can be +90 or -90"""
        self.heading+=angle
    
    def setHeading(self,angle):
        if abs(abs(self.heading) - abs(angle)) == 90 :
            self.heading = angle
    
    def front_pos(self):
        return convert_to_int(self.tims[0].position())
    
    def snake_ate_fruit(self):
        new_tim = Turtle(shape="square")
        new_tim.color('green')
        new_tim.teleport(self.last_pos[0],self.last_pos[1])
        self.tims.append(new_tim)
        self.speed+=1
        self.snake_curr_size+=1
    
    def get_all_pos(self):
        list_pos = set()
        for tim in self.tims:
            list_pos.add(tuple(convert_to_int(tim.pos())))
        return list_pos
    
    def set_speed(self,speed):
        self.speed = speed
    
    def get_snake_size(self):
        return self.snake_curr_size