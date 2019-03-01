from django.shortcuts import render,HttpResponse,render_to_response

# Create your views here.
def hello(request):
    return HttpResponse("hello")

def login(request):
    return(render(request, "WorkingHour/login.html"))