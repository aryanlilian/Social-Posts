# Generated by Django 3.2 on 2021-04-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_rename_post_link_post_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='account',
        ),
        migrations.AddField(
            model_name='post',
            name='social_network',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter')], default='Facebook', max_length=8, verbose_name='Social Network'),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(verbose_name='Link'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
