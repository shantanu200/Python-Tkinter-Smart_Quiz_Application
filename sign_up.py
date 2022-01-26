from database import dbConnect,insert_db,search_db
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
def sign_up():
    
    root.geometry("800x500")
    root.title("SIGN UP HERE")
    root.config(background="white")
    root.resizable(0,0)

    username = ""
    email = ""
    password = ""


    sign_label = Label(root,text="SIGN UP",font=("Code New Roman",24,"bold"),bg="white")
    sign_label.place(x=350,y=50)
            
    username_label = Label(root,text="Username: ",font=("Code New Roman",14,"bold"),bg="white")
    username_label.place(x=275,y=125)
    username = Entry(root,textvariable=username,font=("Code New Roman",12),width=30)
    username.place(x=275,y=150)
            
    email_label = Label(root,text="Email: ",font=("Code New Roman",14,"bold"),bg="white")
    email_label.place(x=275,y=200)
    email = Entry(root,textvariable=email,font=("Code New Roman",12),width=30)
    email.place(x=275,y=225)
            
    password_label = Label(root,text="Password: ",font=("Code New Roman",14,"bold"),bg="white")
    password_label.place(x=275,y=275)
    password = Entry(root,textvariable=password,font=("Code New Roman",12),width=30,show="*")
    password.place(x=275,y=300)

    def sign_in():
        s_username = username.get()
        s_email = email.get()
        s_password = password.get()
    
        if(s_username == '' or s_email == '' or s_password == ''):
            print("All fields are neccessary")

        else:
            if '@' in s_email:
                insert_db(s_username,s_email,s_password)
                mb.showinfo("Success","Data is added to database")
            else:
                mb.showerror("Invalid Email")

    
    signup_button = Button(root,text="SIGN UP",font=("Code New Roman",14,"bold"),bg="green",fg="white",width=15,command=sign_in)
    signup_button.place(x=325,y=350)
    
    app_btn = Button(root,text="APP",font=("Code New Roman",14,"bold"),bg="green",fg="white",width=15,command=go_back)
    app_btn.place(x=325,y=400)
    root.mainloop()


def go_back():
    root.destroy()
    



