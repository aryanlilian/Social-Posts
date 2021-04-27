from django.shortcuts import render
from django.http import HttpResponse


def postsList(request):
    return render(request, 'posts/index.html', {'title': 'This is the first title from the app!'})
