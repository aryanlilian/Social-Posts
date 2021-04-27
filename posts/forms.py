from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author

'''
creating the form for Author objects, for being able to add new Authors in the database from the admin panel
and have all the fields arranget
'''
class AuthorRegistrationForm(UserCreationForm):

    class Meta:
        model = Author
        fields = '__all__'
