from tkinter import *

def submit():
    username = entry.get()
    print("You Entered", username)

def delete():
    entry.delete(0, END)

window = Tk()

entry = Entry(window,
              font= ("arial", 15),
              width=40)

entry.pack(side = TOP)

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
                height =2,
                compound= RIGHT)

delete.pack()

window.mainloop()