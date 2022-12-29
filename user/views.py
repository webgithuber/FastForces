from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from .models import UserDetail
from django.contrib.auth.models import User
from problem.models import Problem ,Submission
import datetime
# Create your views here.

def home(request):
    today=datetime.datetime.now()
    problems=Problem.objects.all()
    lst=[]
    for problem in problems:
        if problem.contest.end_time<today:
            lst.append(problem)
    return render(request,"user/home.html",{"problems":lst,"home":1})

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            UserDetail(user=user).save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render (request,"user/register.html", context={"home":2})

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                user_obj=UserDetail.objects.filter(user=User.objects.get(username=username))
                obj=UserDetail.objects.get(user=User.objects.get(username=username))
                user_obj.update(score=1+obj.score)
                print("testing...",UserDetail.objects.get(user=User.objects.get(username=username)).score)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    return render(request,'user/login.html',{"home":0})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def leaderboard(request):
    user = UserDetail.objects.all().order_by('-score')
    return render(request,'user/leaderboard.html',{'user':user})
def profile(request,user):
    return render(request,'user/profile.html',{'user':User.objects.get(username=user)})

def user_submission(request,user):
    submissions=Submission.objects.filter(user=User.objects.get(username=user)).order_by('-submitted_time')
    return render(request,"user/user_submission.html",{"submissions":submissions,"user_name":user})
    
     