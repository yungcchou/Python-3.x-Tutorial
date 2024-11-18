import tkinter as tk

def on_click():
    print("Button clicked")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("GUI_001") 
    root.geometry("500x400+100+50")

    button = tk.Button( root, 
                        text="Click me", 
                        command=on_click)
    button.pack()

    root.mainloop()
    
