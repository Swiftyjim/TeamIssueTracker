# Generated by Django 3.1.6 on 2022-06-01 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Account',
        ),
    ]
