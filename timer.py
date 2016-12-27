from Tkinter import *
import time

class Timer:

    def __init__(self, master, t_var, task_time=5):
        self.task_length = task_time
        self.root = master
        self.timer_var = StringVar()
        self.timer_label_display(self.root)
        self.start_timer_button(self.root)
                

    def timer_label_display(self, frame):
        """
        Create label on which the countdown timer
        will be displayed
        """
        self.timer_display = Label(
            frame, height=10, width=10, font=16,
            textvariable=self.timer_var
        )
        self.timer_var.set(25)
        self.timer_display.grid(row=0, column=1)

    def start_timer_button(self, frame):
        """ 
        Creates a button that starts the timer
        sequence 
        """
        self.start_button = Button(
            frame, text="Start Timer",
            command=self.start_timer
        )
        self.start_button.grid(row=2, column=0)

    def start_timer(self):
        """ Sets off the timer method """
        mins, secs = divmod(self.task_length, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.timer_var.set(timeformat)
        self.update_timer(self.task_length)

    def update_timer(self, count):
        """ Updates the timer label """
        mins, secs = divmod(count, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.timer_var.set(timeformat)

        if count > 0:
            print timeformat
            self.root.after(1000, self.update_timer, count-1)
        if count == 0:
            self.task_length = 10
            print "Timer done"
    

    
        

        

    

    
        
    
