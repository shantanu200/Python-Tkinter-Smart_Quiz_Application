from database import dbConnect,insert_db,search_db
from tkinter import *
from tkinter import messagebox as mb

root = Tk()

def sign_in():
    root.geometry("800x500")
    root.config(background="white")
    root.title("Sign in")
    root.resizable(0,0)
     
    username = ""
    password = ""

    sign_in = Label(root,text="SIGN IN",font=("Code New Roman",24,"bold"),bg="white")
    sign_in.place(x=325,y=50)

    username_label = Label(root,text="Username: ",font=("Code New Roman",14,"bold"),bg="white")
    username_label.place(x=275,y=125)
    username = Entry(root,textvariable=username,font=("Code New Roman",12),width=30)
    username.place(x=275,y=150)
    
    password_label = Label(root,text="Password: ",font=("Code New Roman",14,"bold"),bg="white")
    password_label.place(x=275,y=200)
    password = Entry(root,textvariable=password,font=("Code New Roman",12),width=30,show="*")
    password.place(x=275,y=225)
    
    def validate_user():
        s_username = username.get()
        s_password = password.get()
        
        if(search_db(s_username,s_password)):
            root.destroy()
            from quiz import quiz_gui
            quiz_gui()


    signin_button = Button(root,text="SIGN IN",font=("Code New Roman",14,"bold"),bg="green",fg="white",width=15,command=validate_user)
    signin_button.place(x=325,y=275)

    def go_signup():
        from sign_up import sign_up
        sign_up()

    signup_button = Button(root,text="SIGN UP",font=("Code New Roman",14,"bold"),bg="purple",fg="white",width=15,command=go_signup)
    signup_button.place(x=600,y=425)
    root.mainloop()
    
def sign_in_destroy():
    root.destroy()

sign_in()