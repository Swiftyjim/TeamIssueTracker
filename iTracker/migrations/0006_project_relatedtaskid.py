# Generated by Django 3.1.6 on 2022-06-10 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0005_auto_20220609_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='relatedTaskID',
            field=models.IntegerField(default=0),
        ),
    ]