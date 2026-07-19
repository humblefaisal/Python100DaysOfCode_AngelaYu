from tkinter import *
from tkinter import ttk

def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    canvas.create_line(lastx, lasty, event.x, event.y)
    savePosn(event)

root = Tk()
root.config(padx=100,pady=100)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(image=logo_img)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

print(root)
root.mainloop()