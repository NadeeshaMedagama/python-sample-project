from tkinter import *
from tkinter import messagebox

def click():

    messagebox.showinfo(title = "Info Message", message = "You Can Access.")
    print("You got Access")

window = Tk()

button = Button(window,
                command = click,
                text = "Click Me!",
                bg="lightgreen",
                fg="red",
                font=("Constantia", 20, "bold"),
                width = 10,
                )

button.pack()

window.mainloop()
