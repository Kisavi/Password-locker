from user import User


def main():

    print("Hello and welcome to password locker. Sign up by filling in the required fields.")
    user_name = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Confirm password: ")

    while password != confirm_password:
        print("Your passwords did not match")
        password = input("Password: ")
        confirm_password = input("Confirm password: ")

    else:
        print(f"{user_name}, your account has been created successfully. Proceed to log in")
        login_user_name = input("Enter your username: ")
        login_password = input("Enter your password: ")

    while login_password != password or login_user_name != user_name:
        print("You have entered a wrong username or password")
        login_user_name = input("Enter your username: ")
        login_password = input("Enter your password: ")

    else:
        print(f"{user_name}, welcome to your account")


main()
