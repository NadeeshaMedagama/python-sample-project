from tkinter import *
from tkinter import messagebox

def click():

    answer = messagebox.askyesnocancel(title = "Yes No Cancel", message = "What is your Decision?", icon = "info")
    if (answer == True):
        print("You Agreed")
    elif(answer == False):
        print("You didn't Agreed")
    else:
        print("You Cancelled!")

window = Tk()

button = Button(window,
                command = click,
                text = "Click Me for get Information!",
                bg="lightgreen",
                fg="red",
                font=("Constantia", 20, "bold")
                 )

button.pack()


window.mainloop()