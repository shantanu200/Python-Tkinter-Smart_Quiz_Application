from database import need_answer, need_options, need_question, get_username,add_score,get_student_score
from tkinter import *
from tkinter import messagebox as mb


quiz = Tk()

num = 0
score = 0
pos_que = 0
neg_que = 0
skip_que = 0
session_username = get_username()
min_label = 0
sec_label = 0
time_text = str(min_label)+":"+str(sec_label)
db_question = []
db_options = []
db_answers = []


def quiz_gui():
    global db_question,db_options,db_answers,session_username,min_label,sec_label,time_text
    quiz.geometry("800x500")
    quiz.title("Quiz-Application")
    quiz.config(background="white")
    quiz.resizable(0, 0)
    quiz_label = Label(quiz, text="QUIZ APPLICATION", width=55,
                       bg="black", fg="white", font=("Code New Roman", 20, "bold"))
    quiz_label.place(x=0, y=2)
    opt_selected = IntVar()
    opt_selected.set(0)
    
    user_score = get_student_score(session_username)
    if(user_score==0):
        db_questions = need_question("smart_quiz")
        db_options = need_options("smart_quiz")
        db_answers = need_answer("smart_quiz")
        min_label = 4
        sec_label = 59
        
    else:
        if(user_score>=20):
            db_questions = need_question("hard_quiz")
            db_options = need_options("hard_quiz")
            db_answers = need_answer("hard_quiz")
            min_label = 3
            sec_label = 59
        
        elif(user_score>=10 and user_score <=20):
            db_questions = need_question("medium-quiz")
            db_options = need_options("medium-quiz")
            db_answers = need_answer("medium-quiz")
            min_label = 3
            sec_label = 59
        
        else:
            db_questions = need_question("smart_quiz")
            db_options = need_options("smart_quiz")
            db_answers = need_answer("smart_quiz")
            min_label = 4
            sec_label = 59


        

    def action_next():
        global num
        try:
            if(num < len(db_questions)):
                check_ans(num)
                num += 1
                get_question(num)
                get_options(num)
                opt_selected.set(0)
        except:
            show_result()
            quiz_over()

    def get_question(que_num):
        que_label.config(text="Q"+str(que_num+1)+". "+db_questions[que_num])

    def get_options(que_num):
        option1.config(text=db_options[que_num]
                       [0], value=1, variable=opt_selected)
        option2.config(text=db_options[que_num]
                       [1], value=2, variable=opt_selected)
        option3.config(text=db_options[que_num]
                       [2], value=3, variable=opt_selected)
        option4.config(text=db_options[que_num]
                       [3], value=4, variable=opt_selected)

    def check_ans(que_num):
        global score, pos_que, neg_que, skip_que
        if(str(opt_selected.get()) == db_answers[que_num]):
            pos_que += 1
            score += 4
        elif(str(opt_selected.get()) != db_answers[que_num] and opt_selected.get() != 0):
            neg_que += 1
            score -= 1
        else:
            skip_que += 1
        print(score)

    def show_result():
        add_score(session_username,score)
        r_score = "Total Score: "+str(score)
        r_pos = "Total Positive: "+str(pos_que)
        r_neg = "Total Negative: "+str(neg_que)
        r_skip = "Total Skip: "+str(skip_que)
        mb.showinfo("Result", "\n".join([r_score, r_pos, r_neg, r_skip]))

    def countdown():
        global min_label, sec_label
        if(min_label >= 0):
            if(sec_label == 0):
                min_label -= 1
                sec_label = 59
            sec_label -= 1
            if(sec_label <= 9):
                fun_time = str(min_label)+":0"+str(sec_label)
            else:
                fun_time = str(min_label)+":"+str(sec_label)
        else:
            show_result()
            quiz_over()

        timer.config(text=fun_time)
        timer.after(1000, countdown)

    time_label = Label(quiz, text="TIME: ", font=(
        "Code New Roman", 14, "bold"), bg="white")
    time_label.place(x=600, y=50)
    timer = Label(quiz, text=time_text, font=(
        "Code New Roman", 14), bg="white")
    timer.place(x=650, y=50)

    que_label = Label(
        quiz, text="Q1. "+db_questions[0], font=("Code New Roman", 16, "bold"), bg="white")
    que_label.place(x=100, y=100)

    option1 = Radiobutton(quiz, text=db_options[0][0], value=1, variable=opt_selected, font=(
        "Code New Roman", 14), bg="white")
    option1.place(x=100, y=150)

    option2 = Radiobutton(quiz, text=db_options[0][1], value=2, variable=opt_selected, font=(
        "Code New Roman", 14), bg="white")
    option2.place(x=100, y=200)

    option3 = Radiobutton(quiz, text=db_options[0][2], value=3, variable=opt_selected, font=(
        "Code New Roman", 14), bg="white")
    option3.place(x=100, y=250)

    option4 = Radiobutton(quiz, text=db_options[0][3], value=4, variable=opt_selected, font=(
        "Code New Roman", 14), bg="white")
    option4.place(x=100, y=300)

    next_btn = Button(quiz, text="NEXT", font=("Code New Roman", 16, "bold"),
                      bg="#648c11", fg="white", width=10, command=action_next)
    next_btn.place(x=250, y=400)

    def exit():
        exitbox = mb.askquestion(
            "Exit Quiz", "You really want to exit", icon="warning")
        if(exitbox == "yes"):
            quiz_over()
        else:
            return None

    end_quiz = Button(quiz, text="EXIT", font=(
        "Code New Roman", 16, "bold"), bg="#ff033e", fg="white", width=10, command=exit)
    end_quiz.place(x=400, y=400)

    countdown()
    quiz.mainloop()


def quiz_over():
    quiz.destroy()

