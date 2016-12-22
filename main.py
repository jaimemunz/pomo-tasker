from Tkinter import *

class App:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.task_list = []

        # Create text widget to display list
        self.task_display = Text(frame, spacing1=1)
        self.task_display.grid(row=0, sticky=N)
        self.task_display.config(state=DISABLED)

        # Entry widget
        self.e = Entry(frame, width = 100)
        self.e.grid(row =1,column=0,sticky=W)

        # Add task button
        self.b = Button(frame, text="Add Task", width=10, command=self.get_entry)
        self.b.grid(row=1, column=2, sticky=W)

        # Quit button
        self.quit_button = Button(
            frame, text = "QUIT", fg="red", command=frame.quit
            )
        self.quit_button.grid(row=2, padx=5, sticky=S)

    def get_entry(self):
        # Gets task from entry widget
        self.task_list.append(self.e.get())
        self.e.delete(0,END)
        self.display_text()

    def display_text(self):
        # Make the text widget editable
        self.task_display.config(state=NORMAL)
        self.task_display.delete(1.0, END)
        for task in self.task_list:
            self.task_display.insert(END, task+ "\n")
        self.task_display.config(state=DISABLED)


root = Tk()
app = App(root)

root.mainloop()
root.destroy()
