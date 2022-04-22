import unittest

from user import User  # import  user class


class TestUser(unittest.TestCase):
    """
    TestUser class defines test cases for the user  class behaviours
    """

    def setUp(self):
        """
        this method allows us to define instructions that will execute before each test case.
        Below, we have instructed our method to create a new instance of User class
        """
        self.new_user = User("James", "w3#g")

    def test_init(self):
        # this method tests if our user object has been instantiated correctly
        self.assertEqual(self.new_user.user_name, "James")
        self.assertEqual(self.new_user.password, "w3#g")

    def test_save_user(self):
        # test if the user object is being added to our user_list
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


# if __name__ == '__main__':
#     unittest.main()
