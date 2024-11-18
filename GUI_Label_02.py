from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01") 
    root.geometry("350x600+100+50")
    label = Label(  root, 
                    text="藉由打造融滲人工智慧與學生生活及學習的一所大學，\
                    逢甲大學將培養出能夠參與社會產業升級轉型的創新人才，\
                    而「人工智慧技術與應用學士學位學程」(以下簡稱為本學程)\
                    的成立，則是其中一個重要環節，並定位於培育應用AI技術解決\
                    實務議題的專業人才",
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

