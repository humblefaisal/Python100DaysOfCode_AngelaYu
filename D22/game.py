from turtle import Turtle,Screen,done
from bar import Bar
from ball import Ball
from constants import *
class GameLoop:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
        self.screen.bgcolor('black')
        self.screen.listen()
        self.screen.tracer(0)
        self.left_bar = Bar(side="left")
        self.right_bar = Bar(side="right")
        self.ball = Ball() 

        self.left_pen = Turtle(visible=False)
        self.left_pen.color("white")
        self.left_pen.teleport(SCORE_LEFT_X,SCORE_Y)
        self.right_pen = Turtle(visible=False)
        self.right_pen.color("white")
        self.right_pen.teleport(SCORE_RIGHT_X,SCORE_Y)

        self.border = Turtle(visible=False)
        self.border.color('white')
        self.border.pensize(PEN_WIDTH)
        self.border.teleport(0,WINDOW_HEIGHT//2)
        self.border.setheading(-90)

        self.draw_dashed_line(length=WINDOW_HEIGHT,stroke_length=STROKE_LENGTH)
        self.loop()
        self.score_left=0
        self.score_right=0
        self.update_score()
        done()

    def draw_dashed_line (self,length,stroke_length):
        tim = self.border
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


    def collision_left(self)->bool:
        if self.ball.x_vel>0 :
            return False
        line_crossed = self.ball.xcor() <= COLL_XMIN
        within_bar = abs(self.ball.ycor() - self.left_bar.ycor() ) <= BAR_SIZE*STRETCHED_WIDTH //2 
        return  line_crossed and within_bar 
    def collision_right(self)->bool:
        if self.ball.x_vel<0 :
            return False
        line_crossed = self.ball.xcor() >= COLL_XMAX
        within_bar = abs(self.ball.ycor() - self.right_bar.ycor()) <= BAR_SIZE*STRETCHED_WIDTH //2
        return  line_crossed and within_bar  
    def collision_wall(self)->bool:
        coll_up   = self.ball.ycor()+BALL_SIZE*BALL_SIZE_FACTOR//2 + BALL_X_VELOCITY >= WINDOW_HEIGHT//2
        coll_down = self.ball.ycor()-BALL_SIZE*BALL_SIZE_FACTOR//2 - BALL_X_VELOCITY <= -WINDOW_HEIGHT//2 
        return  coll_up or coll_down
    def missed_left(self)->bool:
        line_crossed = self.ball.xcor() <= MISS_XMIN
        within_bar = abs(self.ball.ycor() - self.left_bar.ycor() ) <= BAR_SIZE*STRETCHED_WIDTH //2 
        return line_crossed and not within_bar
    def missed_right(self)->bool:
        line_crossed = self.ball.xcor() >= MISS_XMAX
        within_bar = abs(self.ball.ycor() - self.right_bar.ycor()) <= BAR_SIZE*STRETCHED_WIDTH //2
        return  line_crossed and not within_bar  
    def collision_handler(self):
        if self.collision_wall():
            self.ball.y_vel*=-1
        if self.collision_left():
            self.update_ball_velocity(self.left_bar)
        if self.collision_right():
            self.update_ball_velocity(self.right_bar)
        if self.missed_left():
            self.score_right+=1
            self.update_score()
            self.ball.reset()
        if self.missed_right():
            self.score_left+=1
            self.update_score()
            self.ball.reset()

    def update_score(self):
        self.left_pen.clear()
        self.left_pen.write(f"{self.score_left}",align="center",font=('Courier', 30, 'bold'))
        self.right_pen.clear()
        self.right_pen.write(f"{self.score_right}",align="center",font=('Courier', 30, 'bold'))

    def update_ball_velocity(self,bar:Bar):
        self.ball.y_vel += bar.vel
        self.ball.y_vel = min(self.ball.y_vel,BALL_MAX_Y_VEL)
        self.ball.y_vel = max(self.ball.y_vel,-BALL_MAX_Y_VEL)
        self.ball.x_vel *= -1
    
    def loop(self):
        self.collision_handler()
        self.left_bar.update()
        self.right_bar.update()
        self.ball.update()
        self.screen.update()
        self.screen.ontimer(fun=self.loop,t=1000//REFRESH_RATE)
    
        