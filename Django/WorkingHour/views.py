from django.shortcuts import render,HttpResponse,render_to_response
from WorkingHour.utils.ldapAuth import ldapAuth
from WorkingHour.forms import LoginForm
from django import forms

# Create your views here.
def hello(request):
    return HttpResponse("hello")

def login(request):
    return(render(request, "WorkingHour/login.html"))

def index(request):
    try:
        if(request.method == "POST"):
            loginForm = LoginForm(request.POST)
        if(loginForm.is_valid()):
            return(HttpResponse("True"))
        print(type(loginForm.errors))
        for (key, value) in loginForm.errors.items():
            print(key, value)
            return HttpResponse(value)
        
    except forms.ValidationError as e:
        print(e)
        return(HttpResponse(e))
    except Exception as e:
        return(HttpResponse("False"))
