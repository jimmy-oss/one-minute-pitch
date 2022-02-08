import unittest
from app import db
from app.models import MailList

class MailListTest(unittest.TestCase):
    def setUp(self):
        '''
          Set up method to run before each test cases
          '''
        self.new_mail= MailList(email = "jammieoss@gmail.com")
        db.session.add(self.new_mail)
        db.session.commit()

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        MailList.query.delete()
        db.session.commit()
    
    def test_is_instance(self):
       self.assertTrue(isinstance(self.new_mail, MailList))

    def test_save_mail(self):
        '''
        test to check if we can save a email from our blog application 
        '''
        self.new_mail.save_mail()
        self.assertTrue(len(MailList.query.all())>0)