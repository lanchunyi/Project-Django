from django.shortcuts import render,HttpResponse,render_to_response
from WorkingHour.utils.ldapAuth import ldapAuth
from WorkingHour.forms import LoginForm
from django import forms
from .models import User

# Create your views here.
def hello(request):
    return HttpResponse("hello")

def login(request):
    return(render(request, "WorkingHour/login.html"))

def index(request):
    try:
        if(request.method == "POST"):
            loginForm = LoginForm(request.POST)
            print(dir(request.POST))
            print(request.POST.getlist('user'))
            username = request.POST.getlist('user')[0]
            # passwd = request.POST.data['passwd']
            item = User.objects.filter(account=username).values()
            zh_name = item[0]['username']
            print(item)
            print(zh_name)
        if(loginForm.is_valid()):
            return(render_to_response("WorkingHour/index.html", {'username':zh_name}))
        print(type(loginForm.errors))
        for (key, value) in loginForm.errors.items():
            print(key, value)
            return HttpResponse(value)
        
    except forms.ValidationError as e:
        print(e)
        return(HttpResponse(e))
    except Exception as e:
        print(e)
        return(HttpResponse("False"))

