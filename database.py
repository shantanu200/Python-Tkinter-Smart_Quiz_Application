from os import curdir
import re
from turtle import pen
import mysql.connector as mydbconnector

session_username = None


def dbConnect():
    con = mydbconnector.connect(
        host="localhost", username="root", password="", database="python")
    if(con.is_connected() != True):
        print("DataBase Connection Failed")
    else:
        return con


# SIGN UP BACKEND
def insert_db(username, email, password):
    con = dbConnect()
    cursor = con.cursor()
    insert = "INSERT INTO add_data(username,email,password) VALUES(%s,%s,%s)"
    data = (username, email, password)
    cursor.execute(insert, data)
    con.commit()


def set_username(curr_username):
    global session_username
    session_username = curr_username


def get_username():
    return session_username


# SIGN IN BACKEND
def search_db(username, password):
    db_username = []
    db_password = []
    con = dbConnect()
    cursor = con.cursor()
    fetch = """SELECT * FROM add_data WHERE username = %s"""
    result = cursor.execute(fetch, (username,))
    table = cursor.fetchall()
    for row in table:
        g_password = row[3]

    if(password == g_password):
        set_username(username)
        return True
    else:
        return False


def fetch_data(db_name):
    db_options = []
    db_answers = []
    con = dbConnect()
    cursor = con.cursor()
    fetch = "SELECT * FROM "+str(db_name)
    cursor.execute(fetch)
    question = cursor.fetchall()
    return question


def need_question(db_name):
    question = fetch_data(db_name)
    db_questions = []

    for row in question:
        db_questions.append(row[1])

    return db_questions


def need_options(db_name):
    question = fetch_data(db_name)
    db_options = []

    for row in question:
        temp_options = []
        temp_options.append(row[2])
        temp_options.append(row[3])
        temp_options.append(row[4])
        temp_options.append(row[5])
        db_options.append(temp_options)

    return db_options


def need_answer(db_name):
    question = fetch_data(db_name)
    db_answers = []

    for row in question:
        db_answers.append(row[6])

    return db_answers


def add_score(username, score):
    con = dbConnect()
    cursor = con.cursor()
    que = "INSERT INTO score_user(username,score) VALUES(%s,%s)"
    cursor.execute(que, (username, score))
    con.commit()


def modify(string):
    return string.replace(" ", "").replace("?", "").lower()


def easy_insert(user_question, option1, option2, option3, option4, answer):
    con = dbConnect()
    cursor = con.cursor()
    que = "SELECT question FROM smart_quiz"
    cursor.execute(que)
    table = cursor.fetchall()
    easy_question = []
    for row in table:
        easy_question.append(modify(row[0]))
    if(modify(user_question) in easy_question):
        return False
    else:
        data = (user_question, option1, option2, option3, option4, answer)
        insert_data = "INSERT INTO smart_quiz(question,option1,option2,option3,option4,answer) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_data, data)
        con.commit()
        return True


def medium_insert(user_question, option1, option2, option3, option4, answer):
    con = dbConnect()
    cursor = con.cursor()
    que = "SELECT question FROM medium_quiz"
    cursor.execute(que)
    table = cursor.fetchall()
    medium_question = []
    for row in table:
        medium_question.append(modify(row[0]))
    if(modify(user_question) in medium_question):
        return False
    else:
        data = (user_question, option1, option2, option3, option4, answer)
        insert_data = "INSERT INTO medium_quiz(question,option1,option2,option3,option4,answer) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_data, data)
        con.commit()
        return True


def hard_insert(user_question, option1, option2, option3, option4, answer):
    con = dbConnect()
    cursor = con.cursor()
    que = "SELECT question FROM hard_quiz"
    cursor.execute(que)
    table = cursor.fetchall()
    hard_question = []
    for row in table:
        hard_question.append(modify(row[0]))
    if(modify(user_question) in hard_question):
        return False
    else:
        data = (user_question, option1, option2, option3, option4, answer)
        insert_data = "INSERT INTO hard_quiz(question,option1,option2,option3,option4,answer) VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_data, data)
        con.commit()
        return True


def get_student_score(username):
    con = dbConnect()
    cursor = con.cursor()
    que = "SELECT score FROM score_user WHERE username = %s"
    cursor.execute(que, (username,))
    table = cursor.fetchall()
    row_count = 0
    score = 0
    for row in table:
        score = row[0]
        row_count += 1

    return score
