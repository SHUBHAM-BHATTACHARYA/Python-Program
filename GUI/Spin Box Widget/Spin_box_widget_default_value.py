from tkinter import *
window = Tk()
window.title("Welcome ")
window.geometry('350x200')
var =IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin.grid(column=0,row=0)
window.mainloop()

