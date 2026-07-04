import random
from turtle import Turtle,Screen
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SIZE = 20
SCALE_X = 2
SCALE_Y = 1
HALF_CAR_HEIGHT = CAR_SIZE * SCALE_Y // 2
HALF_CAR_WIDTH = CAR_SIZE * SCALE_X // 2
SPAWN_MIN_Y:int = -280 + HALF_CAR_HEIGHT
SPAWN_MAX_Y:int =  280 - HALF_CAR_HEIGHT
HALF_WINDOW_WIDTH = 300

class CarManager:
    def __init__(self):
        self.cars:list = []
        self.spawn_car()
    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
    def spawn_car(self):
        x = HALF_WINDOW_WIDTH - HALF_CAR_WIDTH
        y = random.randint(a=SPAWN_MIN_Y,b=SPAWN_MAX_Y)
        car = Turtle(shape="square")
        car.shapesize(stretch_len=SCALE_X,stretch_wid=SCALE_Y)
        car.teleport(x,y)
        car.setheading(180)
        car.penup()
        car.color(random.choice(COLORS))
        self.cars.append(car)
        # next_car_interval = random.randint(500,2000)
        # car.screen.ontimer(fun=self.spawn_car,t=next_car_interval)
    def collision_bounds(self,car:Turtle):
        (ymin,ymax) = (car.ycor()-HALF_CAR_HEIGHT,car.ycor()+HALF_CAR_HEIGHT)
        (xmin,xmax) = (car.xcor()-HALF_CAR_WIDTH,car.xcor()+HALF_CAR_WIDTH)
        return ((xmin,xmax),(ymin,ymax))
    def get_cars(self):
        return self.cars
    def reset(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []