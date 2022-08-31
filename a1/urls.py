from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="home"),


    path('blog',views.blog,name="blog"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('signup',views.signup,name="signup"),
    path('valt',views.valt,name="valt"),
    path('login',views.login,name="login"),


    
]
