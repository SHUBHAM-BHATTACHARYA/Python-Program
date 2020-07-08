from tkinter import *
from tkinter.ttk import *
window = Tk()
def clicked():
    print(combo.get()) #to get the data from combo box
window.title("Welcome ")
window.geometry('350x200')
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(row=1,column=1)
window.mainloop()
