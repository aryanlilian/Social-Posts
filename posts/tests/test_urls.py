from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import postsList


class TestUrls(SimpleTestCase):

    # The setUp method is for defining all the fields that should be used for testing purposes in the testing methods
    def setUp(self):
        self.posts_list_url = reverse('posts-list')

    # testing the URLs by checking if it's using the right view function for handling the request and responses
    def test_posts_list_url_resolves(self):
        self.assertEquals(resolve(self.posts_list_url).func, postsList)
