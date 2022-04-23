class User:
    """
    This class is a blueprint of user object and generates a new instance of a user
    """
    user_list = []  # empty user list

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        # this method saves a user object in our user_list
        User.user_list.append(self)

    @classmethod
    def display_users(cls):
        return cls.user_list
