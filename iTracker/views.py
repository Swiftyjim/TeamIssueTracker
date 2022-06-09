from ast import Index
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

import iTracker
from .models import *
from django.contrib.auth import authenticate,login, logout
from .auxilary import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        allProj=Project.objects.all()
        allUsers = User.objects.all()
        context={'allProjects':allProj,
            'allUsers':allUsers}
        return render(request,'iTracker/index.html',context)
    else:
        return logInPage(request)

def myPage(request,userName):
    user = User.objects.get(username=userName)
    currentProjects=Project.objects.filter(owner=user)
    context={'currentProjects':currentProjects,
        'user':user}
    return render(request,'iTracker/MyPage.html',context)


def signUpPage(request):
    context={'Teams':Team.objects.all()}
    return render(request,'iTracker/signUPage.html',context)

def register(request):
    firstInput = request.POST['firstName']
    lastInput = request.POST['lastName']
    usernameInput = request.POST['userName']
    passwordInput = request.POST['passWord']
    emailInput = request.POST['email']
    birthdayInput= request.POST['birthday']
    teamInput = request.POST['team']
    user = signUp_aux(usernameInput,passwordInput ,firstInput,lastInput,emailInput,birthdayInput,teamInput)
    login(request,user)
    return myPage(request,usernameINPUT)

def newProjectForm(request):
    return render(request,'iTracker/')

def createNewProj(ownerObj,name,description):
    newProj = Project(
        owner = ownerObj,
        projectName = name,
        description  = description,
    )
    newProj.save()
 

def logInPage(request):
    if request.user.is_authenticated:
        return myPage(request,request.user.username)
    else:
        return render(request,'iTracker/loginPage.html')

def tryLogIn(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Index(request)   
    
    return logInPage(request)

def about(request):
    return render(request,'iTracker/about.html')

def logout_view(request):
    logout(request)
    return render(request,'iTracker/loginPage.html')

def searchButton(request):
    return 1

def thisProject(request,taskID):
    project = Project.objects.get(taskID=taskID)
    user = request.user
    context= {'project':project,'user':user}
    return render(request, 'iTracker/thisProject.html',context)
