from tkinter import *
window = Tk()
window.title("Welcome to SKFGI")
lbl = Label(window, text="Hello",relief=RIDGE,cursor="heart")
lbl.grid(column=0,row=0)
window.geometry('500x500')
window.mainloop() 
