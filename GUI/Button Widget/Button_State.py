from tkinter import *
window = Tk()
window.title("Welcome to SKFGI")
lbl=Button(window,text="Press the Button",bd=100,state=DISABLED)
lbl.grid(column=0,row=0)
window.geometry('500x500')
window.mainloop() 
