import unittest

from credentials import Credentials


class TestCredentials(unittest.TestCase):
    # TestUser class defines test cases for the user  class behaviours

    def setUp(self):
        """
        this method allows us to define instructions that will execute before each test case.
        Below, we have instructed our method to create a new instance of Credentials class
        """
        self.new_credentials = Credentials("Twitter", "pastor", "pass")

    def test_init(self):
        """
        this method tests if our credentials object has been instantiated correctly
        """
        self.assertEqual(self.new_credentials.account, "Twitter")
        self.assertEqual(self.new_credentials.username, "pastor")
        self.assertEqual(self.new_credentials.password, "pass")

    def test_save_credentials(self):
        """
        test if the credentials object is being added to our credentials_list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_credentials_exist(self):
        self.new_credentials.save_credentials()  # saving the new credentials
        test_credentials = Credentials("Instagram", "curly", "pass")  # another new credentials_list
        test_credentials.save_credentials()  # saving the new credentials

        credential_exists = Credentials.credential_exists("Instagram")
        self.assertTrue(credential_exists)

    def test_find_credentials_by_account(self):
        # test if credentials can be searched by account.
        self.new_credentials.save_credentials()  # saving the new credentials
        test_credentials = Credentials("Instagram", "curly", "pass")  # another new credentials_list
        test_credentials.save_credentials()  # saving the new credentials

        found_credential = Credentials.find_by_account(
            "instagram")  # Pass account to find_by_account() to return existing credentials with the same account name
        self.assertEqual(test_credentials.account,
                         found_credential.account
                         )  # Checks if passwords are same from return credentials and created credentials with same account name

    def test_display_all_credentials(self):
        """
        test if nwe are able to return the credentials_list
        """
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credential_list)  # display_credentials() should return the same credentials in our credentials_list

    def test_delete_credentials(self):
        """
        test if we can delete credentials from our list
        """
        self.new_credentials.save_credentials()  # saving the new credentials
        test_credentials = Credentials("Instagram", "curly", "pass")  # another new credentials_list
        test_credentials.save_credentials()  # saving the new credentials

        self.new_credentials.delete_credentials()  # delete a credential object
        self.assertEqual(len(Credentials.credential_list),
                         1)  # Two credentials were saved then one deleted. One credential should be left.


if __name__ == '__main__':
    unittest.main()
