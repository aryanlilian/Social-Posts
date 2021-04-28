from django.shortcuts import render
from .models import Post


def postsList(request):
    posts = Post.objects.all()

    context = {
        'title' : 'Home',
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)
