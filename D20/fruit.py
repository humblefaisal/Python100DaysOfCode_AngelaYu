from turtle import Turtle,Screen
import random
from snake import convert_to_int
from constants import *
def random_point(height:int,width:int):
    rand_x = random.randint(-width//(2*SQUARE_SIZE),width//(2*SQUARE_SIZE))
    rand_y = random.randint(-height//(2*SQUARE_SIZE),height//(2*SQUARE_SIZE))
    return (rand_x,rand_y)

class Fruit :
    def __init__(self,screen:Screen):
        self.screen = screen
        self.tim = Turtle(shape="circle") 
        self.tim.color("red")
        self.screen_width = int(SCREEN_WIDTH) -2*SQUARE_SIZE
        self.screen_height = int(SCREEN_HEIGHT) -2*SQUARE_SIZE
        # rand_x = random.randint(-width//(2*SQUARE_SIZE),width//(2*SQUARE_SIZE))
        # rand_y = random.randint(-height//(2*SQUARE_SIZE),height//(2*SQUARE_SIZE))
        # (rand_x,rand_y) = random_point(height=self.screen_height,width=self.screen_width)
        # self.position = (rand_x*SQUARE_SIZE,rand_y*SQUARE_SIZE)
        # self.tim.teleport(self.position[0],self.position[1]) 
        self.move_random_pos()
        self.update()
    
    def move_random_pos(self):
        (rand_x,rand_y) = random_point(height=self.screen_height,width=self.screen_width)
        self.position = (rand_x*SQUARE_SIZE,rand_y*SQUARE_SIZE)
        self.tim.teleport(self.position[0],self.position[1]) 

    def update(self):
        self.screen.update()
    
    def pos(self):
        return self.position