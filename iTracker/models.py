
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    projectName = models.CharField(max_length=100)
    description = models.CharField(max_length=500,default='Project Description')
    Progressbar = models.IntegerField(default=0)
    taskID = models.AutoField(primary_key=True, editable=False)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.projectName