from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def index(request):
    return redirect("register")

def login(request):
    return HttpResponse("placeholder for users to login")

def register(request):
    return HttpResponse('placeholder for users to create a new user record')

def users(request):
    return HttpResponse('placeholder to later display all the list of users')

def users_new(request):
    return redirect('register')