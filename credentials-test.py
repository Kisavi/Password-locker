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
        # this method tests if our credentials object has been instantiated correctly
        self.assertEqual(self.new_credentials.account, "Twitter")
        self.assertEqual(self.new_credentials.username, "pastor")
        self.assertEqual(self.new_credentials.password, "pass")


if __name__ == '__main__':
    unittest.main()


