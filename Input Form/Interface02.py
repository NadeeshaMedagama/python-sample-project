from tkinter import *

def submit():
    username = entry.get()
    print("You Entered", username)

def delete():
    name0 = entry.get()
    entry.delete(0, END)
    print("You Deleted", name0)

def backspace():
    entry.delete(len(entry.get())-1, END)

def display():
    if(x.get() == 1):
        print ("You are Agreed!")
    else:
        print("You are Not Agreed!")

window = Tk()

window.geometry('500x500')

entry = Entry(window,
              font= ("arial", 15),
              width=40,
              fg ="blue",
              bg = "#ccff33")

entry.pack(side = TOP)

entry2 = Entry(window,
              font= ("arial", 15),
              width=40,
              fg ="blue",
              bg = "#ccff33",
              show = "*")

entry2.pack(side = TOP)

submit = Button(window,
                text = "Submit",
                command = submit,
                width =20,
                height =2)

submit.pack(side = TOP)

delete = Button(window,
                text = "Delete",
                command = delete,
                width =20,
                height =2)

delete.pack()

backspace = Button(window,
                   text = "Backspace",
                   command = backspace,
                   width=20,
                   height=2)

backspace.pack()

x = IntVar()
photo2 = PhotoImage(file ="img_5.png")

check = Checkbutton(window,
                    text = "I Agree to this!",
                    font = ("arial", 15),
                    variable = x,
                    onvalue= 1,
                    offvalue = 0,
                    command = display,
                    fg = "blue",
                    bg = "lightgreen",
                    activeforeground="blue",
                    activebackground="lightgreen",
                    image = photo2,
                    compound = "left")


check.pack()

window.mainloop()