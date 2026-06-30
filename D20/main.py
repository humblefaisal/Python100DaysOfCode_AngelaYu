from turtle import Turtle,Screen,done
from snake import Snake
from fruit import Fruit
from snakegame import SnakeGame,SCREEN_HEIGHT,SCREEN_WIDTH
screen = Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
screen.listen()
screen.onkey(key='Left',fun=lambda : snake.setHeading(180))
screen.onkey(key='Right',fun=lambda : snake.setHeading(0))
screen.onkey(key='Up',fun=lambda : snake.setHeading(90))
screen.onkey(key='Down',fun=lambda : snake.setHeading(-90))
screen.onkey(key='s',fun=lambda : snake.set_speed(1))
screen.onkey(key='f',fun=lambda : snake.set_speed(1000))
screen.onkey(key='p',fun=lambda : snake_game.set_pause())
fruit = Fruit(screen=screen)
snake = Snake(screen=screen)
snake_game = SnakeGame(snake=snake,fruit=fruit,screen=screen)


snake_game.gameLoop()
# while not snake.gameover():
done()