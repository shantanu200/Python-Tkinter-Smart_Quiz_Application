from cgitb import text
import tkinter
from database import need_question,need_answer,need_options
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("TEST_APP")
opt_selected = IntVar()
opt_selected.set(0)
db_questions = need_question()
db_options = need_options()
db_answers = need_answer()
score = 0
num = 0

def action_next():
    global num
    num += 1
    get_questions(num)
    get_options(num)
    check_ans(num)
        
#we need options to fetch:

def get_questions(que_num):
    global db_questions,num
    label.config(text=db_questions[que_num])



def get_options(que_num):
    global db_options
    option1.config(text=db_options[que_num][0],value=1,variable=opt_selected)
    option2.config(text=db_options[que_num][1],value=2,variable=opt_selected)
    option3.config(text=db_options[que_num][2],value=3,variable=opt_selected)
    option4.config(text=db_options[que_num][3],value=4,variable=opt_selected)
    
def check_ans(que_num):
    s = 0
    global db_answers
    if(str(opt_selected.get())==db_answers[que_num]):
        s += 4
    print(s)


   


btn = Button(root,text="Next",font=("Code New Roman",14,"bold"),bg="green",fg="white",command=action_next)
btn.place(x=275,y=350)

label = Label(root,text=db_questions[0],font=("Code New Roman",14,"bold"))
label.place(x=100,y=100)

option1 = Radiobutton(root,text=db_options[0][0],value=1,variable=opt_selected)
option1.place(x=100,y=150)

option2 = Radiobutton(root,text=db_options[0][1],value=2,variable=opt_selected)
option2.place(x=100,y=175)

option3 = Radiobutton(root,text=db_options[0][2],value=3,variable=opt_selected)
option3.place(x=100,y=200)

option4 = Radiobutton(root,text=db_options[0][3],value=4,variable=opt_selected)
option4.place(x=100,y=225)

root.mainloop()



