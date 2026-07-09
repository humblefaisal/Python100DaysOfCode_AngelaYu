import pandas as pd
from turtle import Turtle,Screen,bgpic,done
from constants import *
from _timer import Timer
from quiz import QuizManager
from controller import Controller
screen = Screen()
screen.setup(width=WINDOW_WIDTH,height=WINDOW_HEIGHT)
screen.tracer(0)
bgpic(picname=PICNAME)
timer = Timer()
quiz_manager = QuizManager()
controller = Controller(timer=timer,quiz_manager=quiz_manager)
done()