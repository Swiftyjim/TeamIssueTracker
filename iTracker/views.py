from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'iTracker/index.html')

def myPage(request,idNumber):
    return render(request,'iTracker/MyPage.html',idNumber)

def logIn(request):
    return render(request,'iTracker/loginPage.html')

def about(request):
    return render(request,'iTracker/about.html')