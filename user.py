class User:
    """
    This class is a blueprint of user object and generates a new instance of a user
    """
    user_list = []  # empty user list

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
