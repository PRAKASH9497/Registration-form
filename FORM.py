from tkinter import *
from tkinter import ttk
window=Tk()
window.title("WELCOME TO MY FORM")
window.geometry('1000x600')
window.configure(background = "white");
a = Label(window ,text = "first name").grid(row = 0 ,column = 0)
b = Label(window ,text = "second name").grid(row = 1,column = 0)
c = Label(window ,text ="email id").grid(row = 2,column = 0)
d = Label(window ,text ="password").grid(row = 3,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
def clicked():
    res = "welcome to" + txt.get()
    lbl.configure(text = res)
btn = ttk.Button(window ,text = "submit").grid(row = 4,column = 0)
btn = ttk.Button(window ,text = "reset").grid(row = 5,column = 0)
window.mainloop()