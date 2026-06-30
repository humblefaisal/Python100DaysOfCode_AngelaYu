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
        self.writer:Turtle = Turtle()
        self.writer.hideturtle()
        # self.writer.penup()
        self.writer.color("white")

        
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
            self.writer.goto(GAMEOVER_POS[0],GAMEOVER_POS[1])
            msg = f"GAMEOVER\n"
            self.writer.write(arg=msg,align='center',font=('Arial', 20, 'normal'))

    def snake_ate_fruit(self):
        return self.snake.front_pos() == self.fruit.pos()
            
    def update(self):
        self.screen.update()
        self.update_score()
    
    def gameover(self):
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
        self.writer.clear()
        self.writer.goto(SCORE_POS[0],SCORE_POS[1])
        msg = f"SCORE : {self.score}"
        self.writer.write(arg=msg,font=("Arial",15,"normal"),align="center")