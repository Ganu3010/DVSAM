import string
from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import Contact
import pandas as pd
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . import search as sr
import json

# Create your views here.
def index(request):
    context = {
       
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def loginpage(request):
    return render(request, 'loginpage.html')



def signup(request):
    return render(request, 'signup.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, msg=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')



    

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        # if len(username)<10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('login')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('login')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('login')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def search(request):
    if request.method == 'POST':
        x = sr.Search()
        search_var = request.POST.get('search')
        df = x.search(search_var=search_var)
        json_record = df.reset_index().to_json(orient='records')
        arr = []
        arr = json.loads(json_record)
        context = {'d': arr}
        return render(request, 'filter.html', context=context)
    messages.error('Empty Search Field!')
    return redirect('home')



   

