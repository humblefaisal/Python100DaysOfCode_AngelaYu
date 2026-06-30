from turtle import Turtle,Screen,done

tim = Turtle()
tim.speed(0)
def move_forward():
    global tim
    tim.forward(10)

def move_backward():
    global tim
    tim.backward(10)

def clear():
    global tim
    tim.clear()
    tim.teleport(0,0)
    tim.setheading(0)
    
screen = Screen()
screen.listen()
screen.onkeypress(key='w',fun=move_forward)
screen.onkeypress(key='s',fun=move_backward)
screen.onkeypress(key='d',fun= lambda : tim.right(5))
screen.onkeypress(key='a',fun= lambda : tim.left(5))
screen.onkey(key='c',fun=clear)
done()