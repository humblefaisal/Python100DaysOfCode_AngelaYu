import tkinter as tk
from PIL import Image,ImageTk 
from constants import *
from _timer import Timer


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    timer.reset_timer()
def start_timer():
    global timer
    timer.start_timer()
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timeup_callback():
    global timer
    work_label.config(text=timer.get_mode())
    bring_front()


def bring_front():
    global root
    root.deiconify()
    root.attributes("-topmost",True)
    root.attributes("-topmost",False)


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.minsize(width=500,height=500)
root.config(padx=100,pady=50,bg=YELLOW)
# root.config(bg="tomato.png")
# img = ImageTk.PhotoImage(Image.open("tomato.png"))
# bg_label = tk.Label(image=img)
# bg_label.config(padx=200,pady=200,bg=YELLOW) 
# bg_label.grid(column=1,row=1)

work_label = tk.Label(text="TIMER")
work_label.config(font=(FONT_NAME,40,"normal"),fg=GREEN,bg=YELLOW)
work_label.grid(column=1,row=0)

start_button = tk.Button(text="START")
start_button.config(command=lambda: timer.start_timer())
start_button.grid(column=0,row=2)

reset_button = tk.Button(text="RESET")
reset_button.config(command=lambda: timer.reset_timer())
reset_button.grid(column=2,row=2)

timer = Timer(parent=root,width=200,height=224,timeup_callback=timeup_callback)
timer.grid(row=1,column=1)
root.mainloop()

