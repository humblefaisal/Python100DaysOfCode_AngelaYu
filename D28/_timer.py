import tkinter as tk
from constants import *
class Timer(tk.Label):
    def __init__(self, timeup_callback=None,bg=None):
        super().__init__(bg=None)
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.level = 1 
        self.mode = WORK
        self.running = False
        self.timeup_callback = timeup_callback
        self.config(font=("Courier",20,"bold"))
        self.update_timer()
        # self.start_timer()
    
    def set_timer(self,hours:int=WORK_HOUR,minutes:int=WORK_MIN,seconds:int=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def start_timer(self):
        if not self.hours and not self.minutes and not self.seconds:
            self.set_timer()
        self.running = True
        self.mode=WORK
        self.timeup_callback()
        self.run_timer()
    def pause_timer(self):
        self.running = False
    
    def reset_timer(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.level = 1 
        self.update_timer()
        self.after(func=self.timeup_callback,ms=1000)

    def run_timer(self):
        self.seconds-=1
        if self.seconds<0 :
            self.seconds = 59
            self.minutes -= 1
            if self.minutes < 0:
                self.minutes=59
                self.hours-=1
                if self.hours < 0:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                    if self.mode:
                        if self.level == 4:
                            self.set_timer(hours=0,minutes=LONG_BREAK_MIN)
                        else: 
                            self.set_timer(hours=0,minutes=SHORT_BREAK_MIN)
                    else :
                        self.level+=1
                        if self.level <= 4:
                            self.set_timer()
                        else :
                            self.reset_timer()
                    self.mode = not self.mode
                    self.timeup_callback()
        if self.running:
            self.update_timer()
            self.after(func=self.run_timer,ms=1000)
    
    def update_timer(self):
        label_str = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.config(text=label_str)

    def get_level(self):
        return self.level
    def get_mode(self):
        if not self.running :
            return "TIMER"
        if self.mode:
            return "WORK"
        else :
            return "BREAK"
        