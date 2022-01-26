from tkinter import *
from tkinter import messagebox as mb
from database import need_question,need_options,need_answer

quiz = Tk()
que_num = 0

def quiz_gui():
   

    quiz.geometry("800x500")
    quiz.title("Quiz-Application")
    quiz.config(background="white")
    quiz.resizable(0,0)
    
    quiz_label = Label(quiz,text="QUIZ APPLICATION",bg="white",font=("Code New Roman",24,"bold"))
    quiz_label.place(x=275,y=50)
    
    def all_question(num):
        #Storing the question,options and answers in local variables
        questions = need_question()
        
        answers = need_answer()
    
        question_label = Label(quiz,text=questions[num],font=("Code New Roman",14,"bold"),bg="white")
        question_label.place(x=200,y=150)
   
    def all_options(num):
        options = need_options()
        i = 0
        y_var = 200
        while(i<4):
            option_label = Radiobutton(quiz,text=options[num][i],font=("Code New Roman",14,"bold"),bg="white")
            option_label.place(x=200,y=y_var)
            y_var += 50
            i += 1
    
    def next_data():
        global que_num
        q = que_num
        q += 1
        all_question(que_num)
        all_options(que_num)



    next_button = Button(quiz,text="NEXT",font=("Code New Roman",14,"bold"),bg="green",fg="white",command=next_data)
    next_button.place(x=600,y=400)
    quiz.mainloop()
    
quiz_gui()