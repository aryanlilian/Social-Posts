from django.shortcuts import render
from .models import Post
from .filters import PostFilter


def postsList(request):
    posts = Post.objects.all().order_by('-created_date')
    postsFilter = PostFilter(request.GET, queryset=posts)
    posts = postsFilter.qs

    context = {
        'title' : 'Home',
        'posts' : posts,
        'postsFilter' : postsFilter,
    }
    return render(request, 'posts/index.html', context)
