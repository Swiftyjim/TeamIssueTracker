from django.urls import path, include

from iTracker.auxilary import createNewProj
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('Dashboard/Team/<int:teamID>', views.index, name='index'),
    path('logIn/', views.logInPage, name='logIn'),
    path('signUp/', views.signUpPage, name='signUp'),
    path('signUp/register', views.register, name='register'),
    path('logIn/validate', views.tryLogIn, name='tryLogIn'),
    path('about/', views.about, name='about'),
    path('myPage/logOut', views.logout_view, name='logout_view'),
    path('createNewProject/validate',views.processNewProject,name='processNewProject'),
    path('createNewProject/', views.NewProjectpage,name ='newProjectPage'),
    path('myPage/<str:userName>', views.myPage, name='myPage'),
    path('project/<int:taskID>', views.thisProject, name='projectPage'),
    path('project/<int:taskID>/post', views.postComment, name='postComment'),
    path('project/<int:taskID>/closeTask',views.closeTask,name='closeTask'),
]