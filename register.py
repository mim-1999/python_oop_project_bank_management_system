# User Registration SignIn SignUp
from database import *
from customer import *
from bank import Bank
import random


def SignUp():
    username = input("Create Username: ")
    temp = db_query(
        f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Available..Please Proceed")
        password = input("Enter Password: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(
                f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print(f"Your account Number: {account_number}")
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()


def SignIn():
    username = input("Enter Username: ")
    temp = db_query(
        f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        while True:
            password = input(
                f"Welcome {username.capitalize()}....Enter Password: ")
            temp = db_query(
                f"SELECT password FROM customers WHERE username = '{username}';")
            if temp[0][0] == password:
                print("Signed In Successfully")
                return username
            else:
                print("Wrong password.....Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()
