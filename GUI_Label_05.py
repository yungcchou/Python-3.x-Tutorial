from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01") 
    root.geometry("250x400+100+50")
    labels = []
    bitmaps = ["error", "info", "question", "warning", "questhead", "hourglass"]
    colors = ["#ccddee", "#ffddee", "#ccffdd", "#ccccff", "#99ffcc", "#ddffcc"]
    textVal = " Python "
    reliefs =[ FLAT, GROOVE, RIDGE, SOLID, GROOVE, RAISED]
    compunds = [LEFT, RIGHT, TOP, BOTTOM, CENTER, LEFT]
    for i in range(6):
        labels.append(Label(  root, bitmap=bitmaps[i],
                            width=150, 
                            height=50,
                            bg=colors[i],
                            text=textVal,
                            relief=reliefs[i],
                            compound=compunds[i]).pack(padx=10, pady=5))
    root.mainloop()

