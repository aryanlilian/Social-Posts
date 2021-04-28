from django.shortcuts import render
from .models import Post
from .filters import PostFilter


# The postsList view function is handling the actions which are processing the data to be displayed on the index.html
# file. The index.html file represents the home page of the project
def postsList(request):
    posts = Post.objects.all().order_by('-created_date')
    # postsFilter object is filtering the posts QuerySet that is coming from the db using the parameters from
    # the GET request that is coming from the home page
    postsFilter = PostFilter(request.GET, queryset=posts)
    posts = postsFilter.qs

    # the context HashMap/Dictionary holds all the elements to be sent on the frontend
    context = {
        'title' : 'Home',
        'posts' : posts,
        'postsFilter' : postsFilter,
    }
    return render(request, 'posts/index.html', context)
