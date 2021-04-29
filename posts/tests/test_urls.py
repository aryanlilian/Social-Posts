from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import postsList


class TestUrls(SimpleTestCase):

    def test_posts_list_url_resolves(self):
        url = reverse('posts-list')
        self.assertEquals(resolve(url).func, postsList)
