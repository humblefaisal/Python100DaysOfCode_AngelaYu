from turtle import Turtle

FONT = ("Courier", 24, "normal")
POS = (-250,250)

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.teleport(POS[0],POS[1])
        self.level = 0
        self.update_level()
    def update_level(self):
        self.level+=1
        self.clear()
        self.write(f"Level : {self.level}",font=FONT)
    
