from user import User
from credentials import Credentials
from user import User
from credentials import Credentials
from password_generator import PasswordGenerator


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


def check_existing_credentials(account):
    #  method checks for existence of existing credentials with the provided account name and returns boolean
    return Credentials.credential_exists(account)


def search_credentials(account):
    # method that finds existing credentials by account name
    return Credentials.find_by_account(account)


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

        def start():  # method to be called each time a user wants to perform another task
            response = input("""
            PRESS:
            0 to check your credentials for this account
            1 to create a new credential
            2 to search for credentials by account name
            3 to view existing credentials
            4 to delete a credential
            """)

            if response == "0":
                for user in display_users():
                    print(f"Username: {user.user_name}  Password: {password}")

            elif response == "1":
                password_response = input("""
                Press y if you would like us to generate a random password for you
                n if you would wish to create your own password
                                          """)
                if password_response.lower() == "y":
                    print("Provide the details of the new credentials you wish to create")
                    account = input("Account name: ")
                    username = input("Username: ")
                    pwo = PasswordGenerator()
                    passcode = pwo.generate()

                    save_credentials(create_credentials(account, username, passcode))
                    print(f"New credentials for {account} account created")

                elif password_response.lower() == "n":
                    print("Provide the details of the new credentials you wish to create")
                    account = input("Account name: ")
                    username = input("Username: ")
                    passcode = input("Password: ")

                    save_credentials(create_credentials(account, username, passcode))
                    print(f"New credentials for {account} account created")

                else:
                    print("I really didn't get that. Please use the short codes")

            elif response == "2":
                search_account = input("Enter the account name for the credentials you want to find: ")
                if check_existing_credentials(search_account):
                    found_credentials = search_credentials(search_account)
                    print(f"Account: {found_credentials.account}, Username: {found_credentials.username}, Password: {found_credentials.password}")

                else:
                    print("No search credentials exist")

            def repeat():  # method that allow a user repeat a task or exit the program
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
