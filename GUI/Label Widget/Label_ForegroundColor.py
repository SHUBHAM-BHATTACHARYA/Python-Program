from tkinter import *
window = Tk()
window.title("Welcome to SKFGI")
lbl = Label(window, text="Hello",font ='times 50 underline bold italic',fg='red'
            )
lbl.grid(column=0, row=0)
window.geometry('500x500')
window.mainloop() 
