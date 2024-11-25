from tkinter import *

player = 0

def btn_click( btn ):
    global player
    if btn["text"] == "":
        if player:
            btn.config(text="X", fg="red")
        else:
            btn.config(text="O", fg="blue")

if __name__ == "__main__":
    root = Tk( )
    root.title("Tic Tac Toe")
    root.geometry("300x300+200+100")
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    
    btn00 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn00))
    btn00.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn01 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn01))
    btn01.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn02 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn02))
    btn02.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)
    
    btn10 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn10))
    btn10.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn11 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn11))
    btn11.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn12 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn12))
    btn12.grid(row=1, column=2, sticky=NSEW, pady=2, padx=2)
    
    btn20 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn20))
    btn20.grid(row=2, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn21 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn21))
    btn21.grid(row=2, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn22 = Button(root, text="", font=('Arial', 20),
                    command=lambda: btn_click(btn22))
    btn22.grid(row=2, column=2, sticky=NSEW, pady=2, padx=2)
    
    root.resizable(0, 0)
    root.mainloop()