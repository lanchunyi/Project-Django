from django.shortcuts import render,HttpResponse,render_to_response

# Create your views here.
def hello(request):
    return HttpResponse("hello")

def login(request):
    return(render(request, "WorkingHour/login.html"))

def index(request):
    try:
        user = request.POST['username']
        pwd = request.POST['password']
    except Exception as e:
        return render(request, "WorkingHour/login.html")
    return HttpResponse(user+ "  " + pwd)
