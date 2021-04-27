from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author


# the form is required for being able to perform (CRUD) operations on Author objects on the databse
# and have all the fields arranget
class AuthorRegistrationForm(UserCreationForm):

    class Meta:
        model = Author
        fields = '__all__'
