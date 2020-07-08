from tkinter import *
top = Tk()
C1 = Checkbutton(top, text = "Music" )
C2 = Checkbutton(top, text = "Video")
C1.pack()
C2.pack()
C1.select()
top.mainloop()
