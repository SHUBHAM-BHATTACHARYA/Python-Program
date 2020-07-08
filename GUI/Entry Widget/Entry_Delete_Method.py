from tkinter import*
master=Tk()
def e1_delete():
   e1.delete(first=0,last='end') #if last=20 then it delete 20 character from first
e1=Entry(master, width=100)
e1.pack()
B=Button(master, bd=20,text="del", command=e1_delete)
B.pack()
master.mainloop
