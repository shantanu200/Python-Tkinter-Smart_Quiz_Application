from database import dbConnect,insert_db,search_db
from tkinter import *
from tkinter import messagebox as mb

root = Tk()

def sign_in():
    root.geometry("800x500")
    root.config(background="white")
    root.title("Sign in")
    root.resizable(0,0)

    img = PhotoImage(file="sign_in.png")
    Image_Label = Label(root,image=img,bg="white")
    Image_Label.place(x=50,y=200)
     
    username = ""
    password = ""

    sign_in = Label(root,text="SIGN IN",font=("Code New Roman",24,"bold"),bg="white")
    sign_in.place(x=525,y=50)

    username_label = Label(root,text="Username: ",font=("Code New Roman",14,"bold"),bg="white")
    username_label.place(x=450,y=125)
    username = Entry(root,textvariable=username,font=("Code New Roman",12),width=30)
    username.place(x=450,y=150)
    
    password_label = Label(root,text="Password: ",font=("Code New Roman",14,"bold"),bg="white")
    password_label.place(x=450,y=200)
    password = Entry(root,textvariable=password,font=("Code New Roman",12),width=30,show="*")
    password.place(x=450,y=225)
    
    def validate_user():
        s_username = username.get()
        s_password = password.get()
        
        if(search_db(s_username,s_password)):
            root.destroy()
            from quiz import quiz_gui
            quiz_gui()


    signin_button = Button(root,text="SIGN IN",font=("Code New Roman",14,"bold"),bg="#0000cd",fg="white",width=15,command=validate_user)
    signin_button.place(x=500,y=275)

    def go_signup():
        from sign_up import sign_up
        sign_up()
    root.mainloop()
    
def sign_in_destroy():
    root.destroy()

sign_in()