from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logIn/', views.logIn, name='logIn'),
    path('about/', views.about, name='about'),
    path('<int:idNumber>/myPage', views.myPage, name='myPage'),
]