from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg = colorHex)

window = Tk()

window.geometry('500x500')

button = Button(window,
                text="Click Me",
                command=click,
                bg="lightgreen",
                fg="red",
                font=("Constantia", 20, "bold")
                )

button.pack()

window.mainloop()