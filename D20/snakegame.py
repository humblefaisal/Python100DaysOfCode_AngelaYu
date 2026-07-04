from turtle import Turtle,Screen
from snake import Snake,SQUARE_SIZE
from fruit import Fruit
from constants import *
class SnakeGame:
    def __init__(self,snake:Snake,fruit:Fruit,screen:Screen):
        self.snake = snake
        self.fruit = fruit
        self.screen = screen
        self.pause = False
        self.score:int=0
        self.high_score=0
        with open(HIGH_SCORE_FILE,mode="r") as file:
            self.high_score=int(file.readline())
        self.score_writer:Turtle = Turtle()
        self.score_writer.hideturtle()
        # self.writer.penup()
        self.score_writer.color("white")
        self.score_writer.teleport(SCORE_POS[0],SCORE_POS[1])
        self.writer:Turtle = Turtle()
        self.writer.hideturtle()
        self.writer.color("white")
        self.writer.teleport(GAMEOVER_POS[0],GAMEOVER_POS[1])
        
    def gameLoop(self):
        if not self.pause:
            self.snake.move_forward()
            # string:str
            # if self.snake_ate_fruit():
            #     string = f"{BOLD}{self.snake.front_pos()} : {self.fruit.pos()} : {self.snake_ate_fruit()}{RESET}"
            # else :
            #     string  = f"{self.snake.front_pos()} : {self.fruit.pos()} : {self.snake_ate_fruit()}"
            # print(string)
            if self.snake_ate_fruit():
                self.snake.snake_ate_fruit()
                all_snake_pos = self.snake.get_all_pos()
                while self.fruit.pos() in all_snake_pos:
                    self.fruit.move_random_pos()
                self.score+=1
            
            self.update()
        if not self.gameover():
            movement_speed = self.snake.speed
            self.screen.ontimer(fun=self.gameLoop,t=max(2000//movement_speed,100))  
        else :
            msg = f"GAMEOVER\n"
            if self.high_score<self.score :
                self.high_score=self.score
                with open(HIGH_SCORE_FILE,mode="w") as file:
                    file.write(f"{self.high_score}")
                self.update_score()
            self.writer.write(arg=msg,align='center',font=('Arial', 20, 'normal'))

    def snake_ate_fruit(self):
        return self.snake.front_pos() == self.fruit.pos()
            
    def update(self):
        self.update_score()
        self.screen.update()
    
    def gameover(self)->bool:
        (x,y) = self.snake.front_pos()
        width = SCREEN_WIDTH
        height = SCREEN_HEIGHT
        min_x,min_y = -width/2+SQUARE_SIZE/2,-height/2+SQUARE_SIZE/2
        max_x,max_y = width/2-SQUARE_SIZE/2,height/2-SQUARE_SIZE/2
        unique_pos_count = len(self.snake.get_all_pos())
        snake_overlap = unique_pos_count != self.snake.get_snake_size()
        return x<min_x or y<min_y or x>max_x or y>max_y or snake_overlap

    def set_pause(self):
        self.pause=not self.pause
    
    def update_score(self):
        self.score_writer.clear()
        msg = f"SCORE : {self.score}   HighScore : {self.high_score}"
        self.score_writer.write(arg=msg,font=("Arial",15,"normal"),align="center")
    
    def reset(self):
        self.writer.clear()
        self.score_writer.clear()
        # self.screen.clear()
        # self.screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
        # self.screen.bgcolor("black")
        # self.screen.title("SNAKE GAME")
        # self.screen.tracer(0)
        # self.screen.listen()
        # self.screen.onkey(key='Left',fun=lambda : snake.setHeading(180))
        # self.screen.onkey(key='Right',fun=lambda : snake.setHeading(0))
        # self.screen.onkey(key='Up',fun=lambda : snake.setHeading(90))
        # self.screen.onkey(key='Down',fun=lambda : snake.setHeading(-90))
        # self.screen.onkey(key='s',fun=lambda : snake.set_speed(1))
        # self.screen.onkey(key='f',fun=lambda : snake.set_speed(1000))
        # self.screen.onkey(key='p',fun=lambda : snake_game.set_pause())
        # self.screen.onkey(key='e',fun=lambda : snake_game.reset())
        self.score=0
        self.update_score()
        self.snake.reset()
        self.gameLoop()

