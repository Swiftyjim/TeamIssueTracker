# Generated by Django 3.1.6 on 2022-06-23 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0012_userextended_teamadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='discuss',
        ),
        migrations.AddField(
            model_name='comment',
            name='description',
            field=models.TextField(default='', max_length=1024),
        ),
    ]