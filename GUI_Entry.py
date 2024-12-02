from tkinter import *
from tkinter import ttk

btnRun = None
lab1 = None
input1 = None
input2 = None
def calcualte(  ):
    global lab1, input1, input2, combox1
    if combox1.get() == "+":
        lab1["text"] = str( float(input1.get()) + float(input2.get()) )
    elif combox1.get() == "-":
        lab1["text"] = str( float(input1.get()) - float(input2.get()) )
    elif combox1.get() == "x":
        lab1["text"] = str( float(input1.get()) * float(input2.get()) )
    elif combox1.get() == "/":
        lab1["text"] = str( float(input1.get()) / float(input2.get()) )

if __name__ == "__main__":
    root = Tk()
    root.title("Entry Demo")
    root.geometry("600x50+200+100")
    root.rowconfigure(0, weight=1)
    for i in range( 5 ):
        root.columnconfigure(i, weight=1)
    
    input1 = Entry(root, font=('Arial', 12))
    input1.grid(row=0, column=0, sticky=NSEW)
    
    combox1 = ttk.Combobox(root, values=["+", "-", "x", "/"], width=5)
    combox1.current(0)
    combox1.grid(row=0, column=1, sticky=NSEW)
    
    input2 = Entry(root, font=('Arial', 12))
    input2.grid(row=0, column=2, sticky=NSEW)
    
    btnRun = Button(root, text="=", 
                    font=('Arial', 12),
                    command=calcualte)
    btnRun.grid(row=0, column=3, sticky=NSEW)
    
    lab1 = Label(root, text="0", font=('Arial', 12),
                bg="#ccddee", fg="black", width=10)
    lab1.grid(row=0, column=4, sticky=NSEW)
    
    root.mainloop()
    
    