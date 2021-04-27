from django.urls import path
from .views import postsList


urlpatterns = [
    path('', postsList, name='posts-list'),
]
