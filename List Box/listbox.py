from tkinter import *

def submit():
    if not listbox.curselection():
        print ("You didn't Selected Anyone!")

    else :

        food = []

        for index in listbox.curselection():
            food.insert(index, listbox.get(index))

        print("You Selected: ")

        for index in food:
            print(index)
        print("\n")

def add():

    print("You Added: ", listbox.insert(listbox.size(), entryBox.get()))

    listbox.config(height=listbox.size())

def delete():

    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    print("You Deleted :")

    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg = "#00ccff",
                  font = ("Constantia", 30),
                  width = 15,
                  selectmode= MULTIPLE)

listbox.pack()

listbox.insert(1, "Apple")
listbox.insert(2, "Orange")
listbox.insert(3, "Banana")
listbox.insert(4, "Grapes")
listbox.insert(5, "Pineapple")

listbox.config(height = listbox.size())

entryBox = Entry(window,
                 bg="white",
                 font=("Constantia", 30),
                 width=15)

entryBox.pack()

submit = Button(window,
                text = "Submit",
                command = submit,
                bg= "lightgreen",
                fg = "red",
                font = ("Constantia", 20, "bold"),)

submit.pack()

addBtn = Button(window,
                text = "Add",
                command = add,
                bg="lightgreen",
                fg="red",
                font=("Constantia", 20, "bold"), )

addBtn.pack()

deleteBtn = Button(window,
                text = "Delete",
                command = delete,
                bg="lightgreen",
                fg="red",
                font=("Constantia", 20, "bold"), )

deleteBtn.pack()

window.mainloop()