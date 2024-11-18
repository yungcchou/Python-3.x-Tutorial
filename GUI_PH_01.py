from tkinter import *
from PIL import Image, ImageTk

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01") 
    root.geometry("600x250+100+50")
    img = PhotoImage( file="imgs/cute-and-happy-dog.png")
    describe = """一隻可愛且開心的金毛犬，牠表情開朗，
                看起來非常友善且充滿活力。金毛犬通常以溫暖的
                個性和親和力聞名，非常受人喜愛。牠的毛色金黃，
                耳朵微垂，笑容充滿了愉悅感，這樣的形象很適合
                用於表現快樂和正能量的主題！"""
    lab0 = Label(  root, 
                    image=img, 
                    text=describe,
                    compound=LEFT,
                    bg="#ccddff")
    lab0.pack()
    root.mainloop()
    
    