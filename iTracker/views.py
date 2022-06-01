from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    context=None
    return render(request,'iTracker/index.html')

def myPage(request,idNumber):
    context={'idNumber':idNumber}
    return render(request,'iTracker/MyPage.html',context)

def logIn(request):
    context=None
    return render(request,'iTracker/loginPage.html',context)

def about(request):
    context=None
    return render(request,'iTracker/about.html',context)