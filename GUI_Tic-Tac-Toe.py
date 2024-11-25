from tkinter import *
from tkinter import messagebox

player = 0
def btn_click( btn ):
    global player
    if player:
        btn.config(text="O", fg="blue")
        player = 0
    else:
        btn.config(text="X", fg="red")
        player = 1
    btn.config(state=DISABLED)
    if check_winner():
        messagebox.showinfo("Game Over", "Player " + str(player+1) + " wins!")
        for b in buttons:
            b.config(state=DISABLED)
    elif all([b["text"] != "" for b in buttons]):
        messagebox.showinfo("Game Over", "It's a draw!")
        for b in buttons:
            b.config(state=DISABLED)

def check_winner():
    global buttons
    for i in range(0, 9, 3):
        if buttons[i]["text"] == buttons[i+1]["text"] == buttons[i+2]["text"] != "":
            return True
    for i in range(3):
        if buttons[i]["text"] == buttons[i+3]["text"] == buttons[i+6]["text"] != "":
            return True
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != "":
        return True
    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != "":
        return True
    return False

if __name__ == "__main__":
    root = Tk()
    root.title("Tic Tac Toe")
    root.geometry("300x300+200+100")
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    
    buttons = []
    for i in range(9):
        buttons.append(Button(root, text="", 
                        font=('Arial', 20)))
        buttons[-1].config(command=lambda btn=buttons[-1]: btn_click(btn))
        buttons[-1].grid(row=i//3, column=i%3, 
                    sticky=NSEW, pady=2, padx=2 )
    root.resizable(0, 0)
    root.mainloop()
