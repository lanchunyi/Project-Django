# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, render_to_response

from django.contrib import auth

from WorkingHour.forms import LoginForm
from django import forms
from django.views import View

from .models import User, Project, WorkForm, WorkCount, WorkKinds, FormStream

# Create your views here.


def hello(request):
    return HttpResponse("hello")


def login(request):
    return render(request, "WorkingHour/login.html")


class IndexView(View):
    """
    登录验证view
    """
    def get(self, request):
        return render(request, "WorkingHour/login.html")

    def post(self, request):
        try:
            login_form = LoginForm(request.POST)
            print(dir(request.POST))
            print(request.POST.getlist('user'))
            username = request.POST.getlist('user')[0]
            # passwd = request.POST.data['passwd']
            item = User.objects.filter(account=username).values()[0]
            zh_name = item['username']
            print(item)
            print(zh_name)
            if login_form.is_valid():
                work_count = WorkCount.objects.filter(user_id=str(item['userid']))
                return render_to_response("WorkingHour/index.html", {'user': item, 'work_count': work_count})
            print(type(login_form.errors))
            for (key, value) in login_form.errors.items():
                print(key, value)
                return HttpResponse(value)

        except forms.ValidationError as e:
            print(e)
            return HttpResponse(e)
        except Exception as e:
            print(e)
            return HttpResponse("False")

def index(request):
    try:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            print(dir(request.POST))
            print(request.POST.getlist('user'))
            username = request.POST.getlist('user')[0]
            # passwd = request.POST.data['passwd']
            item = User.objects.filter(account=username).values()
            zh_name = item[0]['username']
            print(item)
            print(zh_name)
        if login_form.is_valid():
            return render_to_response("WorkingHour/index.html", {'username': zh_name})
        print(type(login_form.errors))
        for (key, value) in login_form.errors.items():
            print(key, value)
            return HttpResponse(value)
        
    except forms.ValidationError as e:
        print(e)
        return HttpResponse(e)
    except Exception as e:
        print(e)
        return HttpResponse("False")


def ajax_valid(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        return HttpResponse("{userinfo: lan}")
