# Generated by Django 3.1.6 on 2022-06-09 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0004_userextended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextended',
            name='teamMember',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iTracker.team'),
        ),
    ]
