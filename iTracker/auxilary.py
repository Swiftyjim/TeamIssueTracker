from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login, logout

def signUp_aux(usernameInput,passwordInput ,firstInput,lastInput,emailInput,birthdayInput,teamInput):
    user = User.objects.create_user(
        username = usernameInput,
        password = passwordInput,
        first_name  = firstInput,
        last_name = lastInput,
        email = emailInput
    )
    userExtended = UserExtended(user=user,birthday=birthdayInput,team = teamInput)
    userExtended.save()
    user.save()
    return userExtended

def createNewProj(ownerObj,name,description,tags):
    newProj = Project(
        owner = ownerObj,
        projectName = name,
        description  = description,
        team = ownerObj.team,
        tags = tags,
    )
    newProj.save()
    return newProj

def getUser(username):
    return UserExtended.objects.get(user=User.objects.get(username=username))