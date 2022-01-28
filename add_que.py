from tkinter import *
from tkinter import messagebox as mb
from database import easy_insert, medium_insert, hard_insert

add = Tk()
r_selected = IntVar()
r_selected.set(0)


def add_que():
    add.geometry("800x500")
    add.title("Add Questions")
    add.config(background="white")
    add.resizable(0, 0)
    question = ''
    option1 = ''
    option2 = ''
    option3 = ''
    option4 = ''
    answer = ''

    que_label = Label(add, text="Enter Question: ", font=(
        "Code New Roman", 14, "bold"), bg="white")
    que_label.place(x=100, y=50)

    e_question = Entry(add, textvariable=question,
                       font=("Code New Roman", 14), width=40)
    e_question.place(x=300, y=50)

    option1_label = Label(add, text="Option 1: ", font=(
        "Code New Roman", 14, "bold"), bg="white")
    option1_label.place(x=100, y=100)

    e_option1 = Entry(add, textvariable=option1,
                      font=("Code New Roman", 14), width=40)
    e_option1.place(x=300, y=100)

    option2_label = Label(add, text="Option 2: ", font=(
        "Code New Roman", 14, "bold"), bg="white")
    option2_label.place(x=100, y=150)

    e_option2 = Entry(add, textvariable=option2,
                      font=("Code New Roman", 14), width=40)
    e_option2.place(x=300, y=150)

    option3_label = Label(add, text="Option 3: ", font=(
        "Code New Roman", 14, "bold"), bg="white")
    option3_label.place(x=100, y=200)

    e_option3 = Entry(add, textvariable=option3,
                      font=("Code New Roman", 14), width=40)
    e_option3.place(x=300, y=200)

    option4_label = Label(add, text="Option 4: ", font=(
        "Code New Roman", 14, "bold"), bg="white")
    option4_label.place(x=100, y=250)

    e_option4 = Entry(add, textvariable=option4,
                      font=("Code New Roman", 14), width=40)
    e_option4.place(x=300, y=250)

    answer_label = Label(add, text="Answer(Option No.): ",
                         font=("Code New Roman", 14, "bold"), bg="white")
    answer_label.place(x=100, y=300)

    e_answer = Entry(add, textvariable=answer,
                     font=("Code New Roman", 14), width=40)
    e_answer.place(x=300, y=300)

    difficulty = Label(add, text="Level of Difficulty: ",
                       font=("Code New Roman", 14, "bold"), bg="white")
    difficulty.place(x=100, y=350)
    r1 = Radiobutton(add, value=1, font=("Code New Roman", 14,
                     "bold"), variable=r_selected, text="Easy", bg="white")
    r1.place(x=350, y=350)

    r2 = Radiobutton(add, value=2, font=("Code New Roman", 14,
                     "bold"), variable=r_selected, text="Medium", bg="white")
    r2.place(x=450, y=350)

    r3 = Radiobutton(add, value=3, font=("Code New Roman", 14,
                     "bold"), variable=r_selected, text="Hard", bg="white")
    r3.place(x=550, y=350)

    def validate_question():
        flag = False
        if(e_question.get() != '' and e_option1.get() != '' and e_option2.get() != '' and e_option3.get() != '' and e_option4.get() != '' and e_answer.get() != '' and r_selected.get() != 0):
            if(e_answer.get().isnumeric()):
                if(r_selected.get() == 1):
                    if(easy_insert(e_question.get(), e_option1.get(), e_option2.get(), e_option3.get(), e_option4.get(), e_answer.get()) == True):
                        mb.showinfo(
                            "Success", "Question is Added to data-base")
                        flag = True
                    else:
                        mb.showerror("Error", "Question is already available")
                elif(r_selected.get() == 2):
                    if(medium_insert(e_question.get(), e_option1.get(), e_option2.get(), e_option3.get(), e_option4.get(), e_answer.get()) == True):
                        mb.showinfo(
                            "Success", "Question is Added to data-base")
                        flag = True
                    else:
                        mb.showerror("Error", "Question is already available")
                else:
                    if(hard_insert(e_question.get(), e_option1.get(), e_option2.get(), e_option3.get(), e_option4.get(), e_answer.get()) == True):
                        mb.showinfo(
                            "Success", "Question is Added to data-base")
                        flag = True
                    else:
                        mb.showerror("Error", "Question is already available")
                if(flag):
                    global question, option1, option2, option3, option4, answer
                    question = ''
                    option1 = ''
                    option2 = ''
                    option3 = ''
                    option4 = ''
                    answer = ''
                    r_selected.set(0)

            else:
                mb.showerror("Option error",
                             "Please enter valid option number")
        else:
            mb.showerror("Empty Entry", "All entries are required")

    btn = Button(add, text="ADD QUESTION", font=("Code New Roman",
                 14, "bold"), bg="red", fg="white", command=validate_question)
    btn.place(x=350, y=420)
    add.mainloop()

