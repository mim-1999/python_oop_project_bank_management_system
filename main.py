from register import *
print('Welcome to Mini Banking System')

while True:
    try:
        register = int(input("1. Sign Up\n"
                             "2. Sign In\n"
                             "Enter Option: "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                SignIn()
        else:
            print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input....Try again with valid number")
