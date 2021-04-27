from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# List model represents the lists that will hold the authors/users grouped and will be used for filtering posts
class List(models.Model):
    title = models.CharField(_('Title'), max_length=30, null=False, blank=False)
    created_date = models.DateTimeField(_('Created Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return f'{self.title}'


# Author model represents the people/users that belongs to the Lists and make posts.
# Author class extends the AbstractUser to customize the user model based on the project requirements,
# with this we are able to add fields like 'lists, accounts' and make the authors compatible with the project.
class Author(AbstractUser):
    email = models.EmailField(_('Email'), null=False, blank=False, unique=True)
    first_name = models.CharField(_('First Name'), max_length=100, null=False, blank=False)
    last_name = models.CharField(_('Last Name'), max_length=100, null=False, blank=False)
    # the models.ManyToManyField represents a Many-to-Many relationship between the Author and the List model
    lists = models.ManyToManyField(List)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'


# Account model represents social media accounts that an author/user will have and with which will make posts
class Account(models.Model):

    class SocialNetwork(models.TextChoices):
        FACEBOOK = 'Facebook'
        TWITTER = 'Twitter'

    # the models.ForeignKey represents a One-to-Many relationship between the Account and the Author model.
    # on_delete=models.CASCADE will automatically delete an account when an author/user is deleted from the database
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    username = models.CharField(_('Username'), max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(_('Email'), null=False, blank=False, unique=True)
    social_network = models.CharField(
        _('Social Network'), max_length=8, choices=SocialNetwork.choices, default=SocialNetwork.FACEBOOK
    )
    created_date = models.DateTimeField(_('Created Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.username}/{self.social_network}'


# Post model represents the posts themselves, which will be rendered on the index page
class Post(models.Model):

    # the models.ForeignKey represents a One-to-Many relationship between the Post and the Author & the Post and the Account model.
    # on_delete=models.SET_NULL will keep the post on the database even if an author/user or account is deleted
    # by setting the One-to-Many fields to null
    # db_index it's used to add indexes on the Post table to reduce the time of executing queries
    user = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, db_index=True)
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, db_index=True)
    title = models.CharField(_('Title'), max_length=250, null=False, blank=False, db_index=True)
    content = models.TextField(_('Post content'), null=False, blank=False, db_index=True)
    post_link = models.URLField(max_length=200)
    created_date = models.DateTimeField(_('Created Date/Time'), auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
