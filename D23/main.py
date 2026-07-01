import time
from turtle import Screen,done
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

CAR_SPAWN_PROBABILITY = 1
PLAYER_SIZE = 18
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()
game_is_on = True
speed=0.1
def is_colliding(car_manager:CarManager,player:Player):
    for car in car_manager.get_cars():
        if player.collision(car_manager.collision_bounds(car=car)):
            car.color("black")
            return True
    return False

while game_is_on:
    time.sleep(speed)
    if random.randint(0,100)<CAR_SPAWN_PROBABILITY :
        car_manager.spawn_car()
    car_manager.move_cars()
    if player.crossed_line():
        speed*=0.95
        player.reset()
        car_manager.reset()
        score_board.update_level()

    if is_colliding(car_manager=car_manager,player=player):
        game_is_on=False        
    screen.update()
done()