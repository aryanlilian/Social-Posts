from django.test import TestCase
from posts.models import Author, Post


class BaseTest(TestCase):

    # The setUp method is for defining all the fields that should be used for testing purposes in the testing methods
    def setUp(self):
        self.user_1 = Author.objects.create(
            username='testuser1',
            email='testuser1@mail.com',
            first_name='test',
            last_name='user',
        )
        self.post_1 = Post.objects.create(
            user=self.user_1,
            title='some random title',
            content='some random content',
            social_network='Facebook',
            link='https://www.facebook.com/'
        )


class TestPostModel(BaseTest):

    # testing the Post's model getUserFullName() method by checking if it's returning the correct full name of the parent Author model
    def test_post_model_returning_users_full_name(self):
        self.assertEquals(self.post_1.getUserFullName(), 'test user')
