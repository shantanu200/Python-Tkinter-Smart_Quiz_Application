from cgitb import text
import tkinter
from database import need_question,need_answer,need_options
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("TEST_APP")

db_questions = need_question()
db_options = need_options()
db_answers = need_answer()
rb = tkinter.IntVar()
rb.set(None)
score = 0
num = 0

def action_next():
    global db_answers,db_options,db_questions,num,rb
    fun_num = num
    fun_que = db_questions
    fun_options = db_options
    fun_answer = db_answers
    if(fun_num<len(fun_que)):
        fun_num += 1
        num = fun_num
        label.config(text=fun_que[fun_num])
        rb.set(0)
        get_options(fun_num)
        check_ans(fun_num)
    else:
        print("quiz is over")
        
#we need options to fetch:
def get_options(que_num):
    global db_options,rb
    option1.config(text=db_options[que_num][0],value=1,variable=)
    option2.config(text=db_options[que_num][1],value=2,variable)
    option3.config(text=db_options[que_num][2],value=3,variable=rb)
    option4.config(text=db_options[que_num][3],value=4,variable=rb)
    
def check_ans(que_num):
    global db_answers,score
    if(rb.get()==db_answers[que_num]):
        score+=4
    print(score)
        


btn = Button(root,text="Next",font=("Code New Roman",14,"bold"),bg="green",fg="white",command=action_next)
btn.place(x=275,y=350)

label = Label(root,text=db_questions[num],font=("Code New Roman",14,"bold"))
label.place(x=100,y=100)

option1 = Radiobutton(root,text=db_options[num][0],value=1,variable=rb)
option1.place(x=100,y=150)

option2 = Radiobutton(root,text=db_options[num][1],value=2,variable=rb)
option2.place(x=100,y=175)

option3 = Radiobutton(root,text=db_options[num][2],value=3,variable=rb)
option3.place(x=100,y=200)

option4 = Radiobutton(root,text=db_options[num][3],value=4,variable=rb)
option4.place(x=100,y=225)

root.mainloop()



