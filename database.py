# Banking Database Management
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    username="root",
    password="mim145565",
    database="bank"
)

cursor = mydb.cursor()


def createcustomertable():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                username VARCHAR(20),
                password VARCHAR(20),
                name VARCHAR(20),
                age INTEGER,
                city VARCHAR(20),
                account_number INTEGER,
                status BOOLEAN
                   )
        ''')


def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result


mydb.commit()

if __name__ == '__main__':
    createcustomertable()
