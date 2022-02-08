import unittest # Importing the unittest module
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    '''
    Test class that defines test cases for the Users class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
          Set up method to run before each test cases
          '''
        self.new_user = User(username = "jammie", email ="jammieoss@gmail.com", profile_pic_path = "image_url", password = 'testuser.com')
        db.session.add(self.new_user)
        db.session.commit()

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        User.query.delete()
        db.session.commit()
 
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('testuser.com'))

    def test_save_user(self):
        '''
        test to check if we can save a user from our blog application 
        '''
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

    def test_check_instance_variables(self):
        '''
        test to check if we can find add variables by username,email,profile-pic & password
        '''
        self.assertEquals(self.new_user.username, 'jammie')
        self.assertEquals(self.new_user.email, 'jammieoss@gmail.com')
        self.assertEquals(self.new_user.profile_pic_path, 'image_url')
        self.assertTrue(self.new_user.verify_password('testuser.com'))


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password 