from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01") 
    root.geometry("250x300+100+50")
    labe0 = Label(  root, bitmap="error", 
                    bg="#ccddee", 
                    text=" iSchool, AITA", 
                    compound=LEFT).pack()
    labe1 = Label(  root, bitmap="info", 
                    bg="#ffddee", 
                    text=" iSchool, AITA", 
                    compound="right").pack()
    labe2 = Label(  root, bitmap="question", 
                    bg="#ccffdd", 
                    text=" iSchool, AITA", 
                    compound=TOP).pack()
    labe3 = Label(  root, bitmap="warning", 
                    bg="#ccccff", 
                    text=" iSchool, AITA", 
                    compound="bottom").pack()
    labe4 = Label(  root, bitmap="warning", 
                    bg="#99ffcc", 
                    text=" iSchool, AITA", 
                    compound=CENTER).pack()
    root.mainloop()

