from register import *
from bank import *


print('Welcome to Mini Banking System')

status = False

while True:
    try:
        register = int(input("1. Sign Up\n"
                             "2. Sign In\n"
                             "Enter Option: "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input....Try again with valid number")

account_number = db_query(
    f"SELECT account_number FROM customers WHERE username = '{user}';")


while status:
    print(
        f"Welcome {user.capitalize()}....Choose Banking Service from Below:")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"))
        if facility >= 1 and facility <= 4:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceenquiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receiver = int(
                            input("Enter Receiver Account Number: "))
                        amount = int(input("Enter Money to Transfer: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receiver, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

        else:
            print("Please Enter Valid Input From Options")
            continue

    except ValueError:
        print("Invalid Input....Try again with valid number")
        continue
