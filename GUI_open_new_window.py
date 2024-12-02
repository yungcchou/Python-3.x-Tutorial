from tkinter import *

root = None
def open_new_window():
    global root
    root.withdraw()
    new_window = Toplevel()
    new_window.title("New Window")
    new_window.geometry("300x400+500+100")
    btnBack2root = Button(new_window, text="Back to Root", 
                    font=('Arial', 20),
                    command=lambda: close_window(new_window))
    btnBack2root.pack()
    new_window.mainloop()

def close_window( self ):
    global root
    root.deiconify()
    self.destroy()
        
if __name__ == "__main__":
    root = Tk()
    root.title("Open New Window")
    root.geometry("300x400+200+100")
    
    btnOpen = Button(root, text="Open New Window", 
                    font=('Arial', 20),
                    command=open_new_window)
    btnOpen.pack()
    
    root.mainloop()
    
    
    