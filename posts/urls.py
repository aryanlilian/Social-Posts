from django.urls import path
from .views import postsList


# The urlpatterns array/list is holding all the routes of the posts application and is included in the main
# urls.py file in socialPosts dir, the main dir of the project
urlpatterns = [
    path('', postsList, name='posts-list'),
]
