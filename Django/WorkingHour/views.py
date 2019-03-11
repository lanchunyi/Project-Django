from django.shortcuts import render,HttpResponse,render_to_response
from WorkingHour.utils.ldapAuth import ldapAuth
from WorkingHour.forms import LoginForm

# Create your views here.
def hello(request):
    return HttpResponse("hello")

def login(request):
    return(render(request, "WorkingHour/login.html"))

def index(request):
    try:
        if(request.method == "POST"):
            loginForm = LoginForm(request.POST)
        if(loginForm.is_valid):
            user = loginForm.data["username"]
            pwd = loginForm.data["password"]
        else:
            return render(request, "WorkingHour/login.html")
        auth = ldapAuth(user, pwd)
        # return(HttpResponse("True") if auth.ldapconn() else HttpResponse("False"))
        if(auth.ldapconn()):
            return HttpResponse("True")
        else:
            return HttpResponse("False")
    except Exception as e:
        print(e)
        return render(request, "WorkingHour/login.html")
