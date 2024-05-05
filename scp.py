import json
from customtkinter import *
import tkinter.messagebox

win1=CTk()
#win1.geometry('700x500')
L1=CTkLabel(win1,text='hi it is first LB')
L1.pack()

name=CTkLabel(win1,text='full name')
name.pack()

e1=CTkEntry(win1)
e1.pack()
win1.geometry('300x300')
age=CTkLabel(win1,text='age')
age.pack()
e2=CTkEntry(win1)
e2.pack()
dic1={}
def def1():
    with open ('data.json','w') as f:
        dic1[e1.get()]=e2.get()
        json.dump(dic1,f)
        
        
btn1=CTkButton(win1,text='SUB',state=NORMAL,command=def1,border_width=2,)
btn1.pack()

def def2():
    with open ('data.json','r') as f:
        data=f.readline()
    tkinter.messagebox.showinfo(win1,data)
    
btn2=CTkButton(win1,text='read',command=def2,border_width=2)
btn2.pack()

win1.mainloop()
