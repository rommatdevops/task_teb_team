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


def insert_into_table(login, password, name, nickname):
    mydb = create_connect()
    mycursor = mydb.cursor()
    try:
        sql = "INSERT INTO users (`login`, `password`, `name`, `nickname`) VALUES (%s, %s, %s, %s)"
        val = (login, password, name, nickname)
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as e:
        print('Error write into DB ' + str(e))
        mydb.close()
    