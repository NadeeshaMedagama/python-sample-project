from tkinter import *

count = 0
def click():
    global count
    count+=1
    print ("You clicked the button", count, "times")

window = Tk()
window.geometry('1000x1000')
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

photo1 = PhotoImage(file = "img_3.png")

button = Button(window,
                text = "Click Me!",
                command = click,
                font = ("Comic Sans", 20),
                fg = "#00ff00",
                bg = "black",
                activeforeground= "#00ff00",
                state = ACTIVE,
                image = photo1,
                compound = "bottom")
button.pack()

entry = Entry(window,
              font= ("arial", 15))

entry.pack(side = LEFT)

window.mainloop()