from tkinter import * 
 
main = Tk()
imagePath = D:\Python\GUI(file="Image.JPG")
widgetf = Label(main, image=imagePath).pack(side="right")
comments = """hi"""
widgets = Label(main,  text=comments).pack(side="left")
main.mainloop() 
