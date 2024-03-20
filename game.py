from tkinter import *

root =Tk()
root.geometry("400x450")
root.title("tic tac toe")

frame1=Frame(root)
frame1.pack()
titleLabel=Label(frame1,text="Tic Tac Toe",font=("arial",30),)
titleLabel.pack()

frame2=Frame(root)
frame2.pack()

class tictac():
    def __init__(self):
        self.cells=[" "," "," "," "," "," "," "," "," "]
        self.display()
    def display(self):

        box0=Button(frame2,text=self.cells[0],width=12,height=6)
        box0.grid(row=0,column=0)

        box1=Button(frame2,text=self.cells[1],width=12,height=6)
        box1.grid(row=0,column=1)

        box2=Button(frame2,text=self.cells[2],width=12,height=6)
        box2.grid(row=0,column=2)


        box3=Button(frame2,text=self.cells[3],width=12,height=6)
        box3.grid(row=1,column=0)

        box4=Button(frame2,text=self.cells[4],width=12,height=6)
        box4.grid(row=1,column=1)

        box5=Button(frame2,text=self.cells[5],width=12,height=6)
        box5.grid(row=1,column=2)


        box6=Button(frame2,text=self.cells[6],width=12,height=6)
        box6.grid(row=2,column=0)

        box7=Button(frame2,text=self.cells[7],width=12,height=6)
        box7.grid(row=2,column=1)

        box8=Button(frame2,text=self.cells[8],width=12,height=6)
        box8.grid(row=2,column=2)

Tc= tictac()
Tc.display()
root.mainloop()