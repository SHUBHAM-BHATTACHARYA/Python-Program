from tkinter import*
master=Tk()
def insert1():
  s="skfgi"
  e1.insert(5,s)
e1=Entry(master, width=20)
e1.pack()
B=Button(master, text="click", command=insert1)
B.pack()
master.mainloop
