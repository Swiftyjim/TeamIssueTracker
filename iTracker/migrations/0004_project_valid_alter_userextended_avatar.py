# Generated by Django 4.0.6 on 2022-08-28 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0003_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userextended',
            name='avatar',
            field=models.ImageField(default='static/iTracker/images/default.jpg', upload_to='static/iTracker/images'),
        ),
    ]
