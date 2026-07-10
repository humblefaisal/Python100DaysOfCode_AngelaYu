from turtle import Turtle
from constants import *

class Timer(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.minutes = START_MINUTES
        self.seconds = START_SECONDS
        self.timeup = False
        self.stop_timer = False
        self.heading=0
        self.goto(TIMER_POS_X,TIMER_POS_Y)
        self.color("black")
        self.draw_timer()
        self.screen.ontimer(fun=self.dec_time,t=1000)


    def draw_timer(self):
        self.clear()
        self.write(arg=f"{self.minutes:02d} : {self.seconds:02d}",font=("Arial",TIMER_SIZE,"bold"))
        self.draw_border()
        self.screen.update()
    def draw_border(self,height=TIMER_BORDER_HEIGHT,width=TIMER_BORDER_WIDTH):
        self.forward(width)
        self.left(90)
        self.forward(height)
        self.left(90)
        self.forward(width)
        self.left(90)
        self.forward(height)
        self.left(90)
        return
    def dec_time(self):
        self.seconds-=1
        if self.seconds<0 :
            self.seconds = 59
            self.minutes -= 1
            if self.minutes < 0:
                self.minutes=0
                self.timeup = True
        if not self.timeup and not self.stop_timer:
            self.draw_timer()
            self.screen.ontimer(fun=self.dec_time,t=1000)
    def toggle_timer(self,set_value:bool):
        if set_value == None:
            self.stop_timer = not self.stop_timer
        else :
            self.stop_timer = set_value

    def is_timeup(self):
        return self.timeup
    
        
