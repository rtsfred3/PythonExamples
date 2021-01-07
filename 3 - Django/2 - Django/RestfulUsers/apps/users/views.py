from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import *
if not User.objects.filter(email_address="rtsfred3@gmail.com").exists():
    User.objects.create(first_name="Ryan", last_name="Fred", email_address="rtsfred3@gmail.com")
if not User.objects.filter(email_address="a@a.com").exists():
    User.objects.create(first_name="First_Name", last_name="Last_Name", email_address="a@a.com")

def index(request):
    return render(request,'users/users.html', {'users':User.objects.all()})

def user(request, num=None):
    return render(request, "users/user_id.html", {'id':num, 'user':User.objects.get(id=num)})

def user_edit(request, num=None):
    return render(request, "users/user_update.html", {'id':num, 'user':User.objects.get(id=num)})

def user_delete(request, num=None):
    User.objects.filter(id=num).delete()
    return HttpResponseRedirect('/users/')

def user_new(request):
    return render(request,'users/user_new.html', {})

def user_create(request):
    if request.method == 'POST':
        form = request.POST
        User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email_address=form['email_address'])
    return HttpResponseRedirect('/users/')

def user_update(request):
    if request.method == 'POST':
        form = request.POST
        m = User.objects.get(id=form['id'])
        m.first_name = form['first_name']
        m.last_name = form['last_name']
        m.email_address = form['email_address']
        m.save()
        #User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email_address=form['email_address'])    
    return HttpResponseRedirect('/users/')