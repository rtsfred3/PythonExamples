from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

import re
import bcrypt

from .models import *

NAME_MATCH = re.compile(r'.[^1-9\s]*')
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request,'users/login.html', {})

def success(request):
    return redirect('/wall')

def wall(request):
    context = {'messages':Message.objects.all()}
    return render(request, "users/wall.html", context)

def logoff(request):
    request.session['logged_in'] = False
    request.session['user'] = {}
    return redirect('/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        if len(User.objects.filter(email=email)) > 0 and User.objects.get(email=email):
            user = User.objects.get(email=email)
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['logged_in'] = True
                request.session['user'] = {'id':user.id, 'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email}
                messages.info(request, "You successfully registered (or loggined in)!")
                return redirect('../success')
        return redirect('/')
    return redirect('/')

def register(request):
    if request.method != 'POST':
        return redirect('/')
    
    form = request.POST
    
    if len(User.objects.filter(email=form['email'])) > 0:
        messages.info(request, "There was an error in the registration process")
        return redirect('/')
    
    if len(form['first_name']) < 3 or len(form['last_name']) < 3 or len(form['email']) < 1 or len(form['password']) < 1 or len(form['confirm_password']) < 1 or form['password'] != form['confirm_password'] or (not EMAIL_MATCH.match(form['email']) and len(form['email']) > 0) or (len(form['password']) > 0 and len(form['password']) < 8 and form['password'] == form['confirm_password']):
        if len(form['email']) < 1:
            messages.info(request, "Email cannot be empty!")
        
        if len(form['first_name']) < 1:
            messages.info(request, "First name cannot be empty!")
        elif len(form['first_name']) <= 2:
            messages.info(request, "First name must be more than two letters!")
        
        if len(form['last_name']) < 1:
            messages.info(request, "Last Name cannot be empty!")
        elif len(form['last_name']) <= 2:
            messages.info(request, "Last name must be more than two letters!")        
        
        if len(form['password']) < 1:
            messages.info(request, "Password cannot be empty!")
        
        if len(form['confirm_password']) < 1:
            messages.info(request, "Confirm Password cannot be empty!")
        
        if form['password'] != form['confirm_password']:
            messages.info(request, "Passwords do not match!")
        
        if not EMAIL_MATCH.match(form['email']) and len(form['email']) > 0:
            messages.info(request, "Invalid Email Address!")
        
        if len(form['password']) > 0 and len(form['password']) < 8 and form['password'] == form['confirm_password']:
            messages.info(request, "Password does not meet the minimum length of 8 characters!")
        
        return redirect('/')
    else:
        data = {'first_name': form['first_name'],
                'last_name': form['last_name'],
                'email': form['email'],
                'password': bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        }
        User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])
        u = User.objects.get(email=data['email'])
        request.session['logged_in'] = True
        request.session['user'] = {'id':u.id, 'first_name':data['first_name'], 'last_name':data['last_name'], 'email':data['email']}
        messages.info(request, "You successfully registered (or loggined in)!")
        
        return redirect('../success')

def post_message(request):
    if request.method != 'POST':
        return redirect('/wall/')
    
    form = request.POST
    user = User.objects.get(id=request.session['user']['id'])
    Message.objects.create(user=user, message=form['message'])
    return redirect('/wall/')

def post_comment(request):
    if request.method != 'POST':
        return redirect('/wall/')
    
    form = request.POST
    print(form['comments'])
    Comment.objects.create(user=User.objects.get(id=form['user_id']), message=Message.objects.get(id=form['message_id']), comment=form['comments'])
    return redirect('/wall/')