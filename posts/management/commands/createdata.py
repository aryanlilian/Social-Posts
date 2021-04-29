from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import BaseProvider
from random import sample, randint
from posts.models import List, Author, Post

# The createdate file is generating fake data for the db using the Fake library.

LISTS = [
    'Sport',
    'Education',
    'School',
    'Comedy',
    'Fashio',
    'Toys',
    'Music'
]

SOCIAL_NETWORKS = [
    'Facebook',
    'Twitter'
]


class Provider(BaseProvider):

    def listsTitles(self):
        return self.random_element(LISTS)

    def socialNetworks(self):
        return self.random_element(SOCIAL_NETWORKS)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)

        for _ in range(7):
            list_title = fake.unique.listsTitles()
            List.objects.create(title=list_title)

        for _ in range(100):
            name = fake.name()
            first_name = name.split(' ')[0]
            last_name = ' '.join(name.split(' ')[-1:])
            username = first_name[0].lower() + last_name.lower().replace(' ', '')
            user = Author.objects.create_user(username, password=username)
            user.first_name = first_name
            user.last_name = last_name
            user.is_superuser = False
            user.is_staff = False
            user.email = username + "@" + last_name.lower() + ".com"
            for _ in range(4):
                listsIds = sample(range(1, 11), 4)
                user.lists.add(*listsIds)
            user.save()

        for _ in range(100000):
            user_id = randint(1, 71)
            author = Author.objects.get(id=user_id)
            fake_title = fake.text(max_nb_chars=30)
            fake_content = fake.text(max_nb_chars=150)
            fake_social_network = fake.socialNetworks()
            fake_link='https://www.randomsite.com/'
            Post.objects.create(user=author, title=fake_title, content=fake_content, social_network=fake_social_network, link=fake_link)
