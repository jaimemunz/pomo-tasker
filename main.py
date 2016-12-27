from Tkinter import *
from timer import Timer
import time

class App:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.task_list = []
        self.timer_var = StringVar()
        self.task_time = 25
        self.timer_main = Timer(frame, self.timer_var)

        # Create text widget to display list
        self.task_list_display(frame)
        
        # Entry widget
        self.task_entry(frame)

        # Add task button
        self.add_task_button(frame)

        # Quit button
        self.quit_button(frame)

        
    def task_list_display(self, frame):
        """
        Create the label on which the tasks will be dislpayed
        """
        self.task_display = Text(
            frame, spacing1=1, height=10, width=70
        )
        self.task_display.grid(row=0, column=0, sticky=N)
        self.task_display.config(state=DISABLED)

    def task_entry(self, frame):
        """
        Creates entry widget to add taks to list
        """
        self.e = Entry(frame, width=93)
        self.e.bind("<Return>", self.get_entry)
        self.e.grid(row =1, column=0, sticky=W)

    def add_task_button(self, frame):
        """
        Creates button to add the task in the entry box
        to the list
        """
        self.b = Button(
            frame, text="Add Task", width=16,
            command=self.get_entry
        )
        self.b.grid(row=1, column=1, sticky=W)
    
    def get_entry(self, event=None):
        """ Gets task from entry widget """
        self.task_list.append(self.e.get())
        self.e.delete(0,END)
        self.display_text()
        
    def display_text(self):
        """ Make the text widget editable """
        self.task_display.config(state=NORMAL)
        self.task_display.delete(1.0, END)
        for task in self.task_list:
            self.task_display.insert(END, task+ "\n")
        self.task_display.config(state=DISABLED)

    def quit_button(self, frame):
        """ 
        Creates teh quit button
        """
        self.quit_button = Button(
            frame, text = "QUIT", fg="red",
            command=frame.quit
            )
        self.quit_button.grid(row=3, column=1, padx=5)    
   

root = Tk()
app = App(root)

root.mainloop()
root.destroy()
