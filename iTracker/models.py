
from django.db import models

# Create your models here.
class Account(models.Model):
    userName = models.CharField(max_length=200)
    startDate = models.DateTimeField(auto_now_add=True,editable=False)
    idNumber = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.userName

class Project(models.Model):
    Owner = models.ForeignKey(Account,on_delete=models.CASCADE)
    projectName = models.CharField(max_length=100)
    projectName = models.CharField(max_length=500)
    Progressbar = models.IntegerField(default=0)
    taskID = models.AutoField(primary_key=True, editable=False)
    lastUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project