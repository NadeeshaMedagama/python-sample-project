from tkinter import *
from tkinter import messagebox

def click():

    if messagebox.askokcancel(title = "Your Choice", message = "Are you need to do?"):
        print("You did that.")
    else:
        print("You didn't do that!")


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
