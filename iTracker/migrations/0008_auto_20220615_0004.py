# Generated by Django 3.1.6 on 2022-06-15 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0007_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='taskID',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]