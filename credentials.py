class Credentials:
    """
    This class is a blueprint of credential object and generates a new instance of credentials
    """

    credential_list = []  # our credentials will be saved here by appending when we run the save_credentials method

    def __init__(self, account, username, password):
        """
        here we are creating a new instance of Credentials class
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        """
        method for saving new credentials
        """
        Credentials.credential_list.append(self)

    @classmethod
    def credential_exists(cls, account):
        """
        method that returns boolean depending on the existence of credentials
        """
        for credentials in cls.credential_list:
            if credentials.account == account:
                return True  # returns true if there is credentials with the same account name
        return False

    @classmethod
    def find_by_account(cls, account):
        for credentials in cls.credential_list:
            if credentials.account == account:
                return credentials

    @classmethod
    def display_credentials(cls):
        return cls.credential_list

    def delete_credentials(self):
        Credentials.credential_list.remove(self)
