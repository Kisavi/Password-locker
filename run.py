from user import User
from credentials import Credentials
from user import User
from credentials import Credentials


# user
def create_user(user_name, password):
    new_user = User(user_name, password)
    return new_user


def save_users(user):
    # function to save new user
    user.save_user()


def display_users():
    return User.display_users()


# credentials
def create_credentials(account, username, password):
    new_credentials = Credentials(account, username, password)
    return new_credentials


def save_credentials(credentials):
    credentials.save_credentials()


def display_credentials():
    return Credentials.display_credentials()


def delete_credentials(credentials):
    credentials.delete_credentials()


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
        save_users(create_user(user_name, password))  # create and save new user
        # print(user.password)
        print(f"{user_name}, your account has been created successfully. Proceed to log in")
        login_user_name = input("Enter your username: ")
        login_password = input("Enter your password: ")

    while login_password != password or login_user_name != user_name:
        print("You have entered a wrong username or password")
        login_user_name = input("Enter your username: ")
        login_password = input("Enter your password: ")

    else:
        print(f"{user_name}, welcome to your account")

        def start():
            response = input("""
            PRESS:
            0 to check your credentials for this account
            1 to create a new credential
            2 to view existing credentials
            3 to delete a credential
            """)

            if response == "0":
                for user in display_users():
                    print(f"Username: {user.user_name}  Password: {password}")

            def repeat():
                user_response = input("""
                Would you wish to perform another task? y/n
                """)
                if user_response.lower() == "y":
                    start()
                elif user_response == "n":
                    print("Bye for now")
                else:
                    print("Press y or n")
                    repeat()

            repeat()

        start()


main()
