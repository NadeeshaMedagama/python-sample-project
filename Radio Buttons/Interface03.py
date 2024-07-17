from tkinter import *

food = ["Pizza", "Hotdog", "Rice"]

def order():
    if (x.get()==0):
        print("You ordered Pizza...")
    elif(x.get()==1):
        print("You ordered Hotdog...")
    elif(x.get()==2):
        print("You ordered Rice...")
    else:
        print("huh!")

window = Tk()

photo1= PhotoImage(file ="img_6.png")
photo2= PhotoImage(file ="img_7.png")
photo3= PhotoImage(file ="img_8.png")

foodImages = [photo1, photo2, photo3]

x = IntVar()

for index in range (len(food)):
    radio = Radiobutton(window,
                        text = food[index],
                        variable = x,
                        value =index,
                        padx = 20,
                        pady = 10,
                        font = ('Arial', 30, 'bold'),
                        image = foodImages[index],
                        compound= "right",
                        indicatoron = 0,
                        width = 500,
                        command = order)
    # radio.config()
    radio.pack(anchor ="w")

window.mainloop()