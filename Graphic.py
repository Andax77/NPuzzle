# from tkinter import *
# import random
#
# def CreateWindow(info):
#     root = Tk()
#     i = 0
#     for r in range(info.size):
#         for c in range(info.size):
#           Label(root, text=info.node.get(i), borderwidth=50).grid(row=r,column=c)
#           i += 1
#     root.resizable(False, False)
#     root.mainloop(  )
from tkinter import *

def KeyBoard(event):
    global BalleL,BalleC,LC
    NewL,NewC=BalleL,BalleC
    Key = event.keysym

    if Key == 'Up':
        NewL,NewC=BalleL,BalleC-1

    if Key == 'Left':
        NewL,NewC=BalleL-1,BalleC

    Verification(NewL,NewC)

def Verification(NewL,NewC):
    global BalleL,BalleC,LC

    if LC[NewL][NewC]==0:
        LC[BalleL][BalleC]=0
        BalleL,BalleC=NewL,NewC
        LC[BalleL][BalleC]=2
        MyCanvas.coords(Piece,BalleL*20,BalleC*20 , BalleL*20 +20, BalleC*20 +20)


MyWindow = Tk()
MyWindow.title('Piece')

BalleL = 10
BalleC = 7

MyCanvas = Canvas(MyWindow, width = 400, height =300, bg ='white')
Piece = MyCanvas.create_oval(BalleL*20,BalleC*20,BalleL*20+20,BalleC*20+20,width=2,outline='black',fill='red')
MyCanvas.focus_set()
MyCanvas.bind('<Key>',KeyBoard)
MyCanvas.pack(padx =50, pady =50)

Button(MyWindow, text ='Exit', command = MyWindow.destroy).pack(side=LEFT,padx=5,pady=5)

LC=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

LC[5][5]=1

LC[BalleL][BalleC]=2

print(LC)

i=0
j=0
while j < 15:
    while i<20:
        if LC[j][i]==1:
            MyCanvas.create_rectangle(j*20,i*20,j*20+20,i*20+20,fill='black')
        i=i+1
    i=0
    j=j+1

MyWindow.mainloop()
