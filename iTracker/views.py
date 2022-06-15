from ast import Index
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
import iTracker

from .models import *
from django.contrib.auth import authenticate,login, logout
from .auxilary import *

# Create your views here.
def homePage(request):
    context={}
    return render(request,'iTracker/homePage.html',context)

def index(request,teamID):
    allProjects=Project.objects.filter(team = Team.objects.get(teamID= teamID))
    context={'allProjects':allProjects,'userX':UserExtended.objects.get(user=request.user)}
    return render(request,'iTracker/index.html',context)

def myPage(request,userName):
    if request.user.is_authenticated:
        userX = UserExtended.objects.get(user=User.objects.get(username=userName))
        currentProjects=Project.objects.filter(owner=userX)
        context={'currentProjects':currentProjects,
            'userX':userX}
        return render(request,'iTracker/MyPage.html',context)
    else:
        response = redirect('logIn/')
        return response

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
    user = signUp_aux(usernameInput,passwordInput ,firstInput,lastInput,emailInput,birthdayInput,Team.objects.get(name=teamInput))
    login(request,user)
    return myPage(request,usernameINPUT)


def logInPage(request):
    if request.user.is_authenticated:
        temp = UserExtended.objects.get(user=request.user)
        response = redirect('Dashboard/Team/'+str(temp.team.teamID))
        return response
    else:
        return render(request,'iTracker/loginPage.html')

def tryLogIn(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        temp = UserExtended.objects.get(user =user)
        if user is not None:
            login(request, user)
            
            return myPage(request,user.username)
               
    
    return logInPage(request)

def about(request):
    context={UserExtended.objects.get(user=request.user)}
    return render(request,'iTracker/about.html',context)

def logout_view(request):
    logout(request)
    return render(request,'iTracker/loginPage.html')

def searchButton(request):
    return 1

def thisProject(request,taskID):
    project = Project.objects.get(taskID=taskID)
    user = UserExtended.objects.get(user = request.user)
    comments = Comment.objects.filter(project= project)
    context= {'project':project,'user':user,'comments':comments}
    return render(request, 'iTracker/project.html',context)

def NewProjectpage(request):
    temp =UserExtended.objects.get(user=request.user)
    temp.team
    teams = UserExtended.objects.filter(team = temp.team)
    context={'teams':teams}
    return render(request, 'iTracker/newProject.html',context)

def processNewProject(request):
    projectNameInput = request.POST['projName']
    projectDescriptionInput = request.POST['projDesc']
    projectOwnerInput = request.POST['projOwner']
    createNewProj(UserExtended.objects.get(user=User.objects.get(username=projectOwnerInput)),projectNameInput,projectDescriptionInput)
    currentProjects=Project.objects.filter(owner=UserExtended.objects.get(user=request.user))
    context={
        'currentProjects':currentProjects
    }
    temp=UserExtended.objects.get(user=request.user)
    temp.team.teamID
    return redirect('/iTracker/Dashboard/Team/'+str(temp.team.teamID))

def postComment(request,taskID):
     commentInput = request.POST['comment']
     newPost = Comment(description = commentInput, user = request.user, time = timezone.now, project=Project.objects.get(taskID = taskID)) 
     newPost.save()
     return redirect('/iTracker/project/'+str(taskID))

def closeTask(request,taskID):
    proj = Project.objects.filter(taskID=taskID).delete()
    temp=UserExtended.objects.get(user=request.user)
    temp.team.teamID
    return redirect('/iTracker/Dashboard/Team/'+str(temp.team.teamID))
