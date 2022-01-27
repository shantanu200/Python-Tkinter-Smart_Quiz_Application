# from sign_in import sign_in
# from sign_up import sign_up
from tkinter import *

app = Tk()




def app_gui():
    app.geometry("800x500")
    app.title("Quiz_Application")
    app.resizable(0,0)
    app.config(background="white")

    #adding background image
    img = PhotoImage(file="new-bg.png")
    Image_Label = Label(app,image=img,bg="white")
    Image_Label.pack(pady=(80,0))

    intro_label = Label(app,text="Welcome to QUIZ MANIA!!",font=("Code New Roman",15),bg="white")
    intro_label.place(x=300,y=300)

    signin_btn = Button(app,text="SIGN-IN",bg="blue",fg="white",font=("Code New Roman",15),command=call_signin)
    signin_btn.place(x=320,y=350)

    signup_btn = Button(app,text="SIGN-UP",bg="red",fg="white",font=("Code New Roman",15),command=call_signup)
    signup_btn.place(x=425,y=350)

    leaderboard = Button(app,text="LEADERBOARD",bg="green",fg="white",font=("Code New Roman",15))
    leaderboard.place(x=350,y=400)
    app.mainloop()

def app_destroy():
    app.destroy()

def call_signin():
    app_destroy()
    from sign_in import sign_in
    sign_in()

def call_signup():
    app_destroy()
    from sign_up import sign_up
    sign_up()



app_gui()

