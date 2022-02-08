import unittest
from app.models import Posts
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        '''
          Set up method to run before each test cases
          '''
        self.new_post = Posts(title = "title", post_content= "description", short_description= "Testing testing", post_pic_path="photo_url")
        db.session.add(self.new_post)
        db.session.commit()

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Posts.query.delete()
        db.session.commit()

    def test_save_post(self):
        '''
        test to check if we can post a blog from our blog application 
        '''
        self.new_post.save_post()
        self.assertTrue(len(Posts.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'title')
        self.assertEquals(self.new_post.post_content, 'description')
        self.assertEquals(self.new_post.short_description, 'Testing testing')
    
 