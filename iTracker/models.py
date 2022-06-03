
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    projectName = models.CharField(max_length=100)
    description = models.TextField(max_length=1024,default='Project Description')
    Progressbar = models.IntegerField(default=0)
    taskID = models.AutoField(primary_key=True, editable=False)
    lastUpdate = models.DateTimeField(auto_now=True)
    doing = models.BooleanField(default=False)
    
    def __str__(self):
        return self.projectName

# class Team(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#     description = models.TextField(max_length=1024)
#     logo = models.ImageField()
#     members = models.ForeignKey(UserManager,on_delete=models.CASCADE)

# class UserManager(models.Manager):
#     use_for_related_fields = True

    # def add_player(self, user, team):
    #     # ... your code here ...

    # def remove_player(self, user, team):
        # ... your code here ...
