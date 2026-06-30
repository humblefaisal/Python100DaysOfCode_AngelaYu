import turtle
import numpy as np
from PIL import Image

def draw_imge(image:str):
    turtle.colormode(255)
    def avg_rgb(pixels,x,y):
        pixel = np.array([0,0,0])
        for i in range(PIXEL_SIZE):
            for j in range(PIXEL_SIZE):
                pixel+=pixels[y+i,x+j]
        pixel[0]//=PIXEL_SIZE*PIXEL_SIZE
        pixel[1]//=PIXEL_SIZE*PIXEL_SIZE
        pixel[2]//=PIXEL_SIZE*PIXEL_SIZE
        return pixel.astype(int)

    pixels = np.array(Image.open(image).convert("RGB"))
    PIXEL_SIZE=1
    HEIGHT=pixels.shape[0]//PIXEL_SIZE
    WIDTH=pixels.shape[1]//PIXEL_SIZE
    new_pixels = np.zeros((HEIGHT,WIDTH,3))
    PEN_SIZE=PIXEL_SIZE
    for i in range(HEIGHT):
        for j in range(WIDTH):
            new_pixels[i,j]=avg_rgb(pixels,j*PIXEL_SIZE,i*PIXEL_SIZE)
    pixels=new_pixels
    #Turtle setup
    t=turtle.Turtle()
    screen=t.getscreen()
    screen.tracer(0)
    t.speed(0)
    t.pensize(PEN_SIZE)
    t.shape("square")
    t.penup()
    t.shapesize()
    print(pixels.shape)
    for y in range(pixels.shape[0]):
        t.teleport(-WIDTH/2,HEIGHT/2-y*PEN_SIZE)
        for x in range(pixels.shape[1]):
            r,g,b=pixels[y,x].astype(int)
            t.color((r,g,b))
            t.forward(PEN_SIZE)
            t.stamp()
        screen.update()
    turtle.done()