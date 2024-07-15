from tkinter import *

window = Tk()
window.geometry('500x500')
window.title("My First GUI")

icon = PhotoImage(file = "img.png")
window.iconphoto(True, icon)

photo = PhotoImage(file = "img_1.png")

label = Label(window, text = "Hello World",
              font = ("Arial", 30, 'bold'),
              fg = "blue",
              relief = RAISED,
              bd = 10,
              padx = 10,
              pady = 10,
              image = photo,
              compound = 'bottom')

label.pack()

window.mainloop()