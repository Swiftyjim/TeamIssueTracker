# Generated by Django 3.1.6 on 2022-06-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0014_auto_20220622_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
