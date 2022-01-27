import imp
from tkinter import *

app = Tk()

def app_gui():
    app.geometry("800x500")
    app.title("Quiz_Application")
    app.resizable(0,0)
    app.config(background="white")

    #adding background image
    img = PhotoImage(file=r"new-bg.png")
    Image_quiz = Label(app,image=img,bg="white")
    Image_quiz.pack(pady=(80,50))
    app.mainloop()

app_gui()

