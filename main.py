from Tkinter import *

class App:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.task_list = []

        self.e = Entry(frame, width = 100)
        self.e.pack(side=LEFT)

        self.b = Button(frame, text="get", width=10, command=self.get_entry)
        self.b.pack(side=LEFT)

        self.quit_button = Button(
            frame, text = "QUIT", fg="red", command=frame.quit
            )
        self.quit_button.pack()

    def get_entry(self):
        self.task_list.append(self.e.get())
        self.e.delete(0,END)

root = Tk()
app = App(root)

root.mainloop()
root.destroy()
