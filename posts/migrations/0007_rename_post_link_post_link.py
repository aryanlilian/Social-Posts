# Generated by Django 3.2 on 2021-04-28 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20210427_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_link',
            new_name='link',
        ),
    ]
