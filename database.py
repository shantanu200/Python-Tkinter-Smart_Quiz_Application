import re
import mysql.connector as mydbconnector

session_username = None

def dbConnect():
    con = mydbconnector.connect(host="localhost",username="root",password="",database="python")
    if(con.is_connected()!=True):
        print("DataBase Connection Failed")
    else:
        return con


#SIGN UP BACKEND
def insert_db(username,email,password):
    con = dbConnect()
    cursor = con.cursor()
    insert = "INSERT INTO add_data(username,email,password) VALUES(%s,%s,%s)"
    data = (username,email,password)
    cursor.execute(insert,data)
    con.commit()

def set_username(curr_username):
    global session_username
    session_username = curr_username
    
def get_username():
    return session_username
   

# SIGN IN BACKEND
def search_db(username,password):
    db_username = []
    db_password = []
    con = dbConnect()
    cursor = con.cursor()
    fetch = """SELECT * FROM add_data WHERE username = %s"""
    result =cursor.execute(fetch,(username,))
    table = cursor.fetchall()
    for row in table:
        g_password=row[3]
    
    if(password==g_password):
        set_username(username)
        return True
    else:
        return False 

def fetch_data():
    
    db_options = []
    db_answers = []
    con = dbConnect()
    cursor = con.cursor()
    fetch = "SELECT * FROM smart_quiz"
    cursor.execute(fetch)
    question = cursor.fetchall()
    return question

def need_question():
    question = fetch_data()
    db_questions = []

    for row in question:
        db_questions.append(row[1])
    
    return db_questions


def need_options():
    question = fetch_data()
    db_options = []

    for row in question:
        temp_options = []
        temp_options.append(row[2])
        temp_options.append(row[3])
        temp_options.append(row[4])
        temp_options.append(row[5])
        db_options.append(temp_options)
        
    return db_options

def need_answer():
    question = fetch_data()
    db_answers = []

    for row in question:
        db_answers.append(row[6])
    
    return db_answers


