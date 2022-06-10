
from ast import Delete
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    teamID = models.AutoField(primary_key=True, editable=False)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.name + ': ' + self.description

class UserExtended(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    teamMember = models.ForeignKey(Team,on_delete=models.CASCADE)
    birthday = models.DateTimeField()

    def __str__(self):
        return self.user.username


class Project(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    projectName = models.CharField(max_length=100)
    description = models.TextField(max_length=1024,default='Project Description')
    Progressbar = models.IntegerField(default=0)
    taskID = models.AutoField(primary_key=True, editable=False)
    lastUpdate = models.DateTimeField(auto_now=True)
    doing = models.BooleanField(default=False)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,null=True)
    relatedTaskID = models.IntegerField(default=0)
    discussion = models.ForeignKey(Discussion,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.projectName


    # logo = models.ImageField()
class Discussion(models.Model):
    project = models.ForeignKey(Project,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum.name)

