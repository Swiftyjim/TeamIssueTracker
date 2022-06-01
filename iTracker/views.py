from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login, logout
# Create your views here.
def index(request):
    allProj=Project.objects.all()
    allUsers = User.objects.all()
    context={'allProj':allProj,
        'allUsers':allUsers}
    return render(request,'iTracker/index.html',context)

def myPage(request,userName):
    user = User.objects.get(username=userName)
    currProj=Project.objects.filter(owner=user)
    context={'currProj':currProj,
        'user':user}
    return render(request,'iTracker/MyPage.html',context)


def signUpPage(request):
    context=None
    return HttpResponse('Sign up here')#render(request,'iTracker/loginPage.html',context)

def signUp(usernameINPUT,passwordINPUT,firstINPUT,lastINPUT,emailINPUT):
    user = User.objects.create_user(
        username = usernameINPUT,
        password = passwordINPUT,
        first_name  = firstINPUT,
        last_name = lastInput,
        email = emailINPUT
    )
    user.save()
 

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
    return render(request,'iTracker/loginPage.html')

def tryLogIn(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return myPage(request)   
    
    return logInPage(request)

def about(request):
    return render(request,'iTracker/about.html')

def logout_view(request):
    logout(request)
    return render(request,'iTracker/loginPage.html')

def searchButton(request):
    return 1
