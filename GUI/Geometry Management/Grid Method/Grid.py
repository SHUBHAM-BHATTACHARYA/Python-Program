from tkinter import *
window = Tk()
window.title("Welcome ")
lbl = Label(window, text="Hello")
lbl1 = Label(window, text="Hi")
lbl.grid(row=0,column=2)
lbl1.grid(row=1,column=1)
window.mainloop()
