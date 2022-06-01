from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logIn/', views.logInPage, name='logIn'),
    path('logIn/validate', views.tryLogIn, name='tryLogIn'),
    path('about/', views.about, name='about'),
    path('myPage/<str:userName>', views.myPage, name='myPage'),
    path('myPage/logOut', views.logout_view, name='logout_view'),
]