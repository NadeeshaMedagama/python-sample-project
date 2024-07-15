from tkinter import *

window = Tk()
window.geometry('500x500')
window.title("My First GUI")

icon = PhotoImage(file = "img.png")
window.iconphoto(True, icon)

window.mainloop()