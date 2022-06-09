# Generated by Django 3.1.6 on 2022-06-09 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iTracker', '0002_project_doing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=64, unique=True)),
                ('teamID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1024)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='Project Description', max_length=1024),
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iTracker.team'),
        ),
    ]
