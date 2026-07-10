from quiz import QuizManager
from _timer import Timer
from constants import *
import pandas
class Controller:
    def __init__(self,timer:Timer,quiz_manager:QuizManager):
        self.screen = timer.screen
        self.timer:Timer = timer
        self.quiz_manager:QuizManager = quiz_manager
        self.screen.ontimer(fun=self.gameloop(),t=50)
    def gameloop(self):
        if self.timer.timeup :
            self.quiz_manager.set_gameover()
            not_guessed = [state for state in self.quiz_manager.state_names if state not in self.quiz_manager.get_guessed_states() ]
            data = pandas.Series(not_guessed)
            data.to_csv('Learn_states.csv')
        elif self.quiz_manager.is_game_complete():
            self.timer.toggle_timer(True)
            self.quiz_manager.set_gameover()
            not_guessed = [state for state in self.quiz_manager.state_names if state not in self.quiz_manager.get_guessed_states() ]
            data = pandas.Series(not_guessed)
            data.to_csv('Learn_states.csv')
        else :
            self.screen.ontimer(fun=self.gameloop,t=100)