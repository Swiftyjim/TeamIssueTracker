from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logIn/', views.logInPage, name='logIn'),
    path('signUp/', views.signUpPage, name='signUp'),
    path('signUp/register', views.register, name='register'),
    path('logIn/validate', views.tryLogIn, name='tryLogIn'),
    path('about/', views.about, name='about'),
    path('myPage/logOut', views.logout_view, name='logout_view'),
    path('myPage/<str:userName>', views.myPage, name='myPage'),
    path('project/<int:taskID>', views.thisProject, name='projectPage')
   
]