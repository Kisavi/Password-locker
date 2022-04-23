class Credentials:  # This class is a blueprint of credential object and generates a new instance of credentials

    credential_list = []

    def __init__(self, account, username, password):
        self.account = account
        self.userName = username
        self.password = password

    def save_credentials(self):
        Credentials.credential_list.append(self)
