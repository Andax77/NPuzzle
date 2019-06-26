from tkinter import *

def CreateWindow(info):
    root = Tk()
    for r in range(info.size):
        for c in range(info.size):
          Label(root, text='%s,%s'%(r,c), borderwidth=50).grid(row=r,column=c)
    root.resizable(False, False)
    root.mainloop(  )
