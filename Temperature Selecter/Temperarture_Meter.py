from tkinter import *

def submit():
    print("Temperature is", scale.get(), "degrees C")

window = Tk()

hot = PhotoImage(file ="img_12.png")
hotlabel  = Label(image=hot)
hotlabel.pack()

scale = Scale(window,from_=100,to =0,
              length = 200,
              font = ("Consolas", 20),
              tickinterval = 10,
              troughcolor= "yellow",
              fg = "red",
              bg = "#69faff",
              )

scale.set(35)
# scale.set (((scale["from"]-scale["to"]) / 2) + scale["to"])
scale.pack()

cool = PhotoImage(file ="img_10.png")
coollabel  = Label(image=cool)
coollabel.pack()

button = Button(window,
                command = submit,
                text = "Submit",
                font = ("Consolas", 20),
                )

button.pack()

window.mainloop()