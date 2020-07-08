from tkinter import *
window = Tk()
window.title("Welcome ")
window.geometry('350x200')
spin = Spinbox(window, values=(3, 8, 11), width=5)
spin.grid(column=0,row=0)
window.mainloop()

