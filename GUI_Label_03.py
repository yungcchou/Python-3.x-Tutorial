from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01") 
    root.geometry("350x600+100+50")
    label = Label(  root, 
                    text="In the provided Tkinter code, the Label \
                        component's width and height properties \
                        define the dimensions of the label. The units \
                        of these dimensions are text units, not pixels.",
                    anchor=NW,
                    width=25,
                    height=25,
                    wraplength=100,
                    justify=RIGHT,
                    font=("Times new Roman", 20, "italic", UNDERLINE),
                    background="#ccddff",
                    foreground="#0000ff",)
    label.pack()
    root.mainloop()

