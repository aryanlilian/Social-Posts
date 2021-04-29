from django.test import TestCase, Client
from django.urls import reverse
from posts.models import List, Author, Post


class BaseTest(TestCase):

    # The setUp method is for defining all the fields that should be used for testing purposes in the testing methods
    def setUp(self):
        self.posts_list_url = reverse('posts-list')
        self.list_1 = List.objects.create(title='Cars')
        self.list_2 = List.objects.create(title='Family')
        self.list_3 = List.objects.create(title='IT')
        self.id_filters_for_lists = [1, 2]
        self.user_1 = Author.objects.create(
            username='testuser1',
            email='testuser1@mail.com',
            first_name='test',
            last_name='user',
        )
        self.user_2 = Author.objects.create(
            username='testuser2',
            email='testuser2@mail.com',
            first_name='test',
            last_name='user',
        )
        self.user_1.lists.add(*[self.list_1, self.list_2])
        self.user_2.lists.add(*[self.list_3])
        self.post1 = Post.objects.create(
            user=self.user_1,
            title='some random title',
            content='some random content',
            social_network='Facebook',
            link='https://www.facebook.com/'
        )
        self.post2 = Post.objects.create(
            user=self.user_1,
            title='some random title 2',
            content='some random content 2',
            social_network='Facebook',
            link='https://www.facebook.com/'
        )
        self.post3 = Post.objects.create(
            user=self.user_2,
            title='some random title 3',
            content='some random content 3',
            social_network='Twitter',
            link='https://www.twitter.com/'
        )


class TestPostsListView(BaseTest):

    # testing the GET requests and response for the postsList view function by checking if it's returning the right status code
    def test_posts_list_view_GET(self):
        response = self.client.get(self.posts_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/index.html')

    # testing the POST requests and response for the postsList view function by checking if the filters are working correctly
    def test_posts_list_view_POST_filtering(self):
        posts_filtered_by_title = Post.objects.filter(title__icontains='some random').count()
        posts_filtered_by_content_incorect = Post.objects.filter(content__icontains='cnt').count()
        posts_filtered_by_content_corect = Post.objects.filter(content__icontains='content 3').count()
        posts_filtered_by_title_and_social_network = Post.objects.filter(
            title__icontains='some random title', social_network='Facebook').count()
        users_filtered_by_lists = Author.objects.filter(lists__in=self.id_filters_for_lists)
        posts_filtered_by_users_lists = Post.objects.filter(user__in=users_filtered_by_lists).count()

        self.assertEquals(posts_filtered_by_title, 3)
        self.assertEquals(posts_filtered_by_content_incorect, 0)
        self.assertEquals(posts_filtered_by_content_corect, 1)
        self.assertEquals(posts_filtered_by_title_and_social_network, 2)
        self.assertEquals(posts_filtered_by_users_lists, 2)
