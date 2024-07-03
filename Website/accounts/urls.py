from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.User_login , name='user_login'),
    path('user_logout/', views.user_logout , name='user_logout'),
    path('register/' , views.user_register , name='user_register'),
    path('Userprofile/' , views.Userprofile, name='Userprofile')  ,
]