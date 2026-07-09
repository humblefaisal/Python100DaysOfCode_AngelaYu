from turtle import Turtle,textinput
import pandas
from constants import *
class QuizManager(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.state_data = pandas.read_csv(FILENAME)
        self.guessed_states:set = set()
        self.total_states = len(self.state_data.state)
        self.state_names = set(self.state_data.state)
        self.game_complete = False
        self.gameover = False
        self.prompt()

    def prompt(self):
        title = f"{len(self.guessed_states)}/{self.total_states} States Correct"
        state_name = textinput(title=title,prompt="Guess a state name :")
        if type(state_name) == None :
            return
        state_name = state_name.title()
        if state_name not in self.guessed_states and state_name in self.state_names : 
            state_row = self.state_data[self.state_data.state == state_name]
            (x,y) = (int(state_row.x),int(state_row.y))
            self.goto(x,y)
            self.write(state_name)
            self.guessed_states.add(state_name)
        if len(self.guessed_states) < self.total_states and not self.gameover:
            self.screen.ontimer(fun=self.prompt,t=50)
        else :
            self.game_complete = True
    def is_game_complete(self):
        return self.game_complete
    def set_gameover(self):
        self.gameover = True