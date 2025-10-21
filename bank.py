# Bank Services
from database import *
import datetime


class Bank():

    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(f'''
CREATE TABLE IF NOT EXISTS {self.__username}_transaction
(timedate VARCHAR(30),
account_number INTEGER,
remarks VARCHAR(30),
amount INTEGER)
''')

    def balanceenquiry(self):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}'")
        print(f"Your Current Balance is: {temp[0][0]}")

    def deposit(self, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}' ")
        test = temp[0][0] + amount
        db_query(
            f"UPDATE customers SET balance = {test} WHERE username = '{self.__username}'")
        self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Account Deposit',"
                 f"'{amount}')"
                 )
        print(f"{self.__username}...Amount is Successfully Deposited into Your Account {self.__account_number}")

    def withdraw(self, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}' ")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            test = temp[0][0] - amount
        db_query(
            f"UPDATE customers SET balance = {test} WHERE username = '{self.__username}'")
        self.balanceenquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Account Withdraw',"
                 f"'{amount}')"
                 )
        print(
            f"{self.__username}...Amount is Successfully Withdrawed from Your Account{self.__account_number}")

    def fundtransfer(self, receiver, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}' ")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            temp2 = db_query(
                f"SELECT balance FROM customers WHERE account_number = '{receiver}' ")
            if temp2 == []:
                print("Account Number Does not Exists")
            else:
                test1 = temp[0][0] - amount
                test2 = amount + temp2[0][0]
                db_query(
                    f"UPDATE customers SET balance = {test1} WHERE username = '{self.__username}'")
                db_query(
                    f"UPDATE customers SET balance = {test2} WHERE account_number = '{receiver}'")
                receiver_username = db_query(
                    f"SELECT username FROM customers WHERE account_number = '{receiver}' ")
                self.balanceenquiry()
                db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{receiver}',"
                         f"'Fund Received from {self.__account_number}',"
                         f"'{amount}')"
                         )
                db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer -> {receiver}',"
                         f"'{amount}')"
                         )
        print(
            f"{self.__username}...Amount is Successfully Transferred  from Your Account: {self.__account_number} to User: {receiver_username[0][0]} and Account No: {receiver}")
