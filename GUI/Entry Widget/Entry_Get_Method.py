from tkinter import*
master=Tk()
def e1_data():
    s=e1.get()
    l=Label(master,text=s)
    l.pack()
e1=Entry(master, width=100)
e1.pack()
B=Button(master,text="click", command=e1_data)
B.pack()
master.mainloop
