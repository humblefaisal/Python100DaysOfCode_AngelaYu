from turtle import Turtle,Screen
from constants import *
class Bar(Turtle):
    def __init__(self,side):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_len=STRETCHED_LEN,stretch_wid=STRETCHED_WIDTH)
        self.color('white')
        self.side:int = 0
        if(side=="left") :
            self.side = -1
            self.set_key_events(up="w",down="s")
        if(side=="right") :
            self.side = 1
            self.set_key_events(up="Up",down="Down")
        self.X_POS = self.side*WINDOW_WIDTH*REL_POSITION // 2 - self.side * BAR_SIZE*STRETCHED_LEN // 2
        self.y=0
        self.vel = 0
        self.accn = 0
        self.update()
    
    def set_key_events(self,up:str,down:str):
        self.key_up:str = up  
        self.key_down:str = down
        self.screen.onkeypress(key=up,fun=self.move_up)
        self.screen.onkeypress(key=down,fun=self.move_down)
        self.screen.onkeyrelease(key=up,fun=self.reset_accn)
        self.screen.onkeyrelease(key=down,fun=self.reset_accn)
    def move(self):
        self.vel += self.accn
        self.vel = min(self.vel,BAR_MAX_VEL)
        self.vel = max(self.vel,-BAR_MAX_VEL)
        if (self.y + self.vel + BAR_SIZE * STRETCHED_WIDTH / 2  < WINDOW_HEIGHT / 2) and self.vel > 0:
            self.y+=self.vel / DELTA
        elif (self.y + self.vel - BAR_SIZE * STRETCHED_WIDTH / 2  > -WINDOW_HEIGHT / 2) and self.vel < 0:
            self.y+=self.vel / DELTA
        else :
            self.vel = 0 
        if(self.vel != 0) :
            self.vel= max((abs(self.vel)-FRICTION),0) * self.vel / abs(self.vel)
        # self.vel=0
    def move_up(self):
        self.accn=ACCN
    def move_down(self):
        self.accn=-ACCN 
    def reset_accn(self):
        self.accn=0
    def update(self):
        self.move()
        self.goto(self.X_POS,self.y)
        # self.screen.ontimer(fun=self.update,t=(1000//REFRESH_RATE))
        # self.screen.update()
