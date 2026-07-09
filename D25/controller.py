from quiz import QuizManager
from _timer import Timer

class Controller:
    def __init__(self,timer:Timer,quiz_manager:QuizManager):
        self.screen = timer.screen
        self.timer:Timer = timer
        self.quiz_manager:QuizManager = quiz_manager
    def gameloop(self):
        if self.timer.timeup :
            self.quiz_manager.set_gameover()
        if self.quiz_manager.is_game_complete():
            self.timer.toggle_timer(True)
        self.screen.ontimer(fun=self.gameloop,t=100)