from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLLISION_BOX_HALF_SIDE = 8 ## half side 

class Player(Turtle):
    def __init__(self, shape = "turtle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.setheading(90)
        self.penup()
        self.teleport(STARTING_POSITION[0],STARTING_POSITION[1])
        self.screen.onkeypress(key="Up",fun=self.move)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def crossed_line(self):
        return self.ycor()>=FINISH_LINE_Y
    def collision(self,collision_bounds):
        (ymin,ymax) = (self.ycor()-COLLISION_BOX_HALF_SIDE,self.ycor()+COLLISION_BOX_HALF_SIDE)
        (xmin,xmax) = (self.xcor()-COLLISION_BOX_HALF_SIDE,self.xcor()+COLLISION_BOX_HALF_SIDE)
        ((cxmin,cxmax),(cymin,cymax)) = collision_bounds

        # return y >= ymin and y <= ymax and x >= xmin and x <=xmax
        return cxmin <= xmax and cxmax >= xmin and cymin <= ymax and cymax >= ymin
    def reset(self):
        self.teleport(STARTING_POSITION[0],STARTING_POSITION[1])

    