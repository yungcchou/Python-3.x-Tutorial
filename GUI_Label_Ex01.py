from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01") 
    root.geometry("250x300+100+50")
    labels = []
    bitmaps = ["error", "info", "question", "warning", "hourglass"]
    colors = ["#ccddee", "#ffddee", "#ccffdd", "#ccccff", "#99ffcc"]
    textVal = " iSchool, AITA"
    reliefs =[RAISED, SUNKEN, FLAT, RIDGE, GROOVE]
    for i in range(5):
        labels.append(Label(  root, bitmap=bitmaps[i],
                            bg=colors[i],
                            text=textVal,
                            compound=compunds[i]).pack())
    root.mainloop()

