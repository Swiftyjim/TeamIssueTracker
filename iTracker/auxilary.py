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
    AddInfo = UserExtended(user=user,birthday=birthdayInput,teamMember = teamInput)
    AddInfo.save()
    user.save()
    return user

def createNewProj(ownerObj,name,description):
newProj = Project(
    owner = ownerObj,
    projectName = name,
    description  = description,
)
newProj.save()