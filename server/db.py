import mysql.connector
import config

def create_connect():
    mydb = mysql.connector.connect(
        host=config.host,
        user=config.user,
        passwd=config.passwd,
        database=config.database
    )
    return mydb


def check_login_pass_in_db(login):
    mydb = create_connect()
    try:
        mycursor = mydb.cursor()
    except Exception as e:
        print('Cannot connect to db ' + str(e))
    try:
        mycursor.execute("SELECT * FROM users WHERE login = (%s)", (login,))
        myresult = mycursor.fetchall()
        print(myresult)
        if myresult != []:
            print("Login exists:", myresult[0][2])
        else:
            print("Login not found")
            return False
    except Exception as e:
        print('Some error: ' + str(e))

    try:
        mycursor.execute("SELECT password FROM users WHERE login = (%s)", (login,))
        myresult = mycursor.fetchall()
        if myresult != []:
            password = myresult[0][0]
            return password
        else:
            print("Password wrong")
            return False
    except Exception as e:
        print('Cannot execute query or: ' + str(e))


def select_name_nick(login):
    mydb = create_connect()
    try:
        mycursor = mydb.cursor()
    except Exception as e:
        print('Cannot connect to db ' + str(e))
    try:
        mycursor.execute("SELECT name, nickname FROM users WHERE login = (%s)", (login,))
        myresult = mycursor.fetchall()
        if myresult != []:
            return myresult
        else:
            print("Login not found")
            return False
    except Exception as e:
        print('Some error: ' + str(e))

    
