from tkinter import *
window = Tk()
window.title("Welcome to SKFGI")
lbl = Label(window, text="Hello",bg="red",fg="white",underline=4)
lbl.grid(column=0,row=0)
window.geometry('500x500')
window.mainloop() 
