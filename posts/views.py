from django.shortcuts import render, redirect
from .models import Post, List, Author
from .utils import getValuesFromRequest


# The postsList view function is handling the actions which are processing the data to be displayed on the
# index.html file. The index.html file represents the home page of the project
def postsList(request):
    # getting all the List objects from the db in descending order for being displayed on the form
    lists = List.objects.all().order_by('-created_date')

    if request.method == 'POST':
        # getting the inputs values from the POST request of the filtering form
        title, content, socialNetworks, startDate, endDate, peopleList = getValuesFromRequest(request)

        # getting the filtered authors objects by the lists form the db
        authors = Author.objects.filter(lists__in=peopleList) if peopleList else Author.objects.all()
        # getting the filtered Posts objects by the filtering form from the db
        posts = Post.objects.filter(
            user__in=authors, title__icontains=title, content__icontains=content,
            social_network__in=socialNetworks, created_date__range=[startDate, endDate]
        ).order_by('-created_date')
    else:
        posts = Post.objects.all().order_by('-created_date')

    # the context HashMap/Dictionary holds all the elements to be sent on the frontend
    context = {
        'title' : 'Home',
        'posts' : posts,
        'lists' : lists,
    }
    return render(request, 'posts/index.html', context)
