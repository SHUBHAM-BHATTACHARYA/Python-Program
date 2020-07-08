from tkinter import*
master=Tk()
def move_cursor():
  e1.icursor ( 5 )
e1=Entry(master, width=20)
e1.pack()
B=Button(master, text="click", command=move_cursor)
B.pack()
master.mainloop
