from django.urls import path, include

from iTracker.auxilary import createNewProj
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('Dashboard/Team/<int:teamID>', views.index, name='index'),

    path('logIn/validate', views.tryLogIn, name='tryLogIn'),
    path('logIn/', views.logInPage, name='logIn'),

    path('signUp/', views.signUpPage, name='signUp'),
    path('signUp/register', views.register, name='register'),

    
    path('about/', views.about, name='about'),
    
    path('createNewProject/validate',views.processNewProject,name='processNewProject'),
    path('createNewProject/', views.NewProject,name ='newProject'),

    path('myPage/<str:userName>', views.myPage, name='myPage'),
    path('myPage/logOut', views.logout_view, name='logout_view'),

    path('project/<int:taskID>', views.thisProject, name='projectPage'),
    path('project/<int:taskID>/post', views.postComment, name='postComment'),
    path('project/<int:taskID>/closeTask',views.closeTask,name='closeTask'),
    path('project/<int:taskID>/openTask',views.openTask,name='openTask'),
    path('project/<int:taskID>/assign',views.assignOwner,name='assignOwner'),
    path('project/<int:taskID>/status',views.updateStatus,name='updateStatus'),
    path('project/<int:taskID>/editProject',views.editProject,name='editProject'),
    path('project/<int:taskID>/save',views.saveProject,name='saveProject'),
    
]