from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, List, Post
from .forms import AuthorRegistrationForm


# registering the models on the admin side, will allow to see, apply (CRUD operations) from the admin panel

@admin.register(Author)
class AuthorAdmin(UserAdmin):
    model = Author
    add_form = AuthorRegistrationForm
    list_display = ['__str__', 'is_superuser', 'is_staff', 'is_active', 'date_joined']

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User\'s Lists',
            {
                'fields': (
                    'lists',
                )
            }
        ),
    )


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)
