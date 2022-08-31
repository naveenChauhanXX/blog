from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import Feature
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def home(request):
    
    return render (request,"index.html")

def blog(request):
    
    
    features = Feature.objects.all()
    return render(request,"blog.html",{'features':features})

def about(request):
    return render(request,"about.html")



def contact(request):
    return render(request,"contact.html")

def signup(request):
        if request.method =="POST":

            username= request.POST['username']

            email= request.POST['email']

            pass1 = request.POST['pass1']

            

            myuser = User.objects.create_user(username, email, pass1 )
            myuser.user_name=username

            myuser.save()
            messages.success(request,"account created successfully")
            return redirect('home')




        return render (request,"signup.html")



def valt(request):
   return render(request,"valt.html")


def login(request):
    if request.method == "POST" :
        username = request.POST['username']

        pass1 = request.POST['pass1']


        user = authenticate(username=username ,pass1=pass1)
        if user is not None:
                    login(request,user)
                    username= user.user_name
                    return render(request,"valt",{'username':username})

        else:
            messages.error(request,"bad credentionals")
            return redirect('home')
                

    return render(request,"login.html")


    
