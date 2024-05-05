import json
import tkinter
from tkinter import *
import tkinter.messagebox

win1=Tk()
win1.geometry('700x500')
L1=Label(win1,text='hi it is first LB',fg='red',padx=100,pady=100)
L1.pack()

name=Label(win1,text='full name')
name.pack()

e1=Entry(win1)
e1.pack()

age=Label(win1,text='age')
age.pack()

e2=Entry(win1)
e2.pack()
dic1={}
def def1():
    with open ('data.json','w') as f:
        dic1[e1.get()]=e2.get()
        json.dump(dic1,f)
        
        
btn1=Button(win1,text='SUB',fg='red',state=NORMAL,command=def1)
btn1.pack()

def def2():
    with open ('data.json','r') as f:
        data=f.readline()
    tkinter.messagebox.showinfo(win1,data)

btn2=Button(win1,text='read',fg='blue',command=def2)
btn2.pack()

win1.mainloop()
