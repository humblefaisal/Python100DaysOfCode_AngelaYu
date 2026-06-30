from turtle import Turtle,Screen,done
import random
MAX_STEPS = 20
FINISH_LINE = 300

screen = Screen()
screen.colormode(255)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def run(tim:Turtle):
    tim.forward(random.randint(0,MAX_STEPS))
def setup(tim:Turtle,shape:str,position:tuple):
    # tim.speed(0)
    tim.shape(shape)
    tim.color(random_color())
    tim.teleport(position[0],position[1])

def start_race(tims:list):
    winner=None
    while winner is None:
        for tim in tims:
            run(tim)
            if tim.xcor()>= FINISH_LINE:
                winner=tim
    for index,tim in enumerate(tims):
        if(tim is winner):
            return index
    return -1

setup(tim=t1,shape='turtle',position=(-300,150))
setup(tim=t2,shape='turtle',position=(-300,50))
setup(tim=t3,shape='turtle',position=(-300,-50))
setup(tim=t4,shape='turtle',position=(-300,-150))

tims = [t1,t2,t3,t4]
choice = int(screen.numinput(title="BET",prompt="Chose you turtle",default=0,minval=0,maxval=3))
winner = start_race(tims)
if(winner == choice):
    tims[choice].write("You WON")
else :
    tims[choice].write("You Lost")

done()