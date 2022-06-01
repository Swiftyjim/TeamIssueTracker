
from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=200)
    startDate = models.DateTimeField('date published')
    idNumber = models.AutoField(primary_key=True)

    def __str__(self):
        return self.userName

class Projects(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.CharField(max_length=200)
    Progressbar = models.IntegerField(default=0)

    def __str__(self):
        return self.project