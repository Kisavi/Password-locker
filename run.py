from user import  User

def main():

    response = input(
        """
        Hello and welcome to password locker. Instructions to navigate. PRESS:
        1 to Sign up
        2 to Login to your account
        3 to create custom passwords
        4 to generate random passwords
        5 to view saved credentials
        6 to delete a credential 
        """
    )

    if response == "1":
        print("Fill in the required fields to Signup")
        user_name = input("Username: ")
        password = input("Password: ")
        confirm_password = input("Confirm password: ")



