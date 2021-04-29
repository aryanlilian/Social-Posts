# Social Posts

First steps to do when setting the Social Posts project on your local machine with Django

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
MacOS
    $ source project-env/bin/activate
Windows
    $ cd project-env/Scripts/activate
$ git clone https://github.com/aryanlilian/Social-Posts.git
$ cd Social-Posts
$ pip install -r requirements.txt

# You may want to change the name `project-env`.
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


I've built the Social Media Lists project using Python and Django framework for the backend and on the frontend, I've used basic HTML/CSS/Bootstrap-5 to have a simple and interactive UI/UX for the user.

The database tables are split between Authors who represents the users that made the social posts on social networks, the Post table where are stored all the posts which are displayed on the home page, and the last one the List table where are stored all lists of that users make part of, like some categorizations.

Even though in the requirements of the project is said to not build and admin panel but just generate fake data, the project has an admin panel and an SQLite database connected because the Django framework provides those by default and when I made the migrations on the database the admin panel was created automatically and I used it for efficiently handling the data.

Features that I've implementing:
    1. Used database table indexes for making the queries more efficient and fast.
    2. Filtering the model objects from the database using Django's ORMs.
    3. Used an MVT architecture for a better representation of the project's files and directories, which is very similar to the MVC.
    4. Implementing the backend infrastructure for displaying and filtering the database models.
    5. Implementing Unit Tests for the ULRs, Views and Models.
    6. Used the Faker library for generating the fake data.
