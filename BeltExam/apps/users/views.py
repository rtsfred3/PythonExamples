from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from django.core import serializers

import re
import json
import bcrypt

from apps.users.models import *

NAME_MATCH = re.compile(r'.[^1-9\s]*')
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request,'users/login.html', {})

def success(request):
    if request.session['logged_in'] and request.session['user'] != {}:
        user = User.objects.get(id=request.session['user']['user_id'])
        request.session['user'] = {'user_id':user.id, 'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email}
    return redirect('/quotes')

def logoff(request):
    if request.method == 'POST':
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
                request.session['user'] = {'user_id':user.id, 'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email}
                messages.info(request, "You successfully registered (or loggined in)!")
                return redirect('../success')
        messages.info(request, "There was an error with logging in")
        return redirect('/')
    return redirect('/')

def register(request):
    if request.method != 'POST':
        return redirect('/')
    
    form = request.POST
    
    if len(form['first_name']) < 3 or len(form['last_name']) < 3 or len(form['email']) < 1 or len(form['password']) < 1 or len(form['confirm_password']) < 1 or form['password'] != form['confirm_password'] or (not EMAIL_MATCH.match(form['email']) and len(form['email']) > 0) or (len(form['password']) > 0 and len(form['password']) < 8 and form['password'] == form['confirm_password']):
        if len(form['email']) < 1:
            messages.error(request, "Email cannot be empty!")
        
        if len(form['first_name']) < 1:
            messages.error(request, "First name cannot be empty!")
        elif len(form['first_name']) <= 2:
            messages.error(request, "First name must be more than two letters!")
        
        if len(form['last_name']) < 1:
            messages.error(request, "Last name cannot be empty!")
        elif len(form['last_name']) <= 2:
            messages.error(request, "Last name must be more than two letters!")        
        
        if len(form['password']) < 1:
            messages.error(request, "Password cannot be empty!")
        
        if len(form['confirm_password']) < 1:
            messages.error(request, "Confirm Password cannot be empty!")
        
        if form['password'] != form['confirm_password']:
            messages.error(request, "Passwords do not match!")
        
        if not EMAIL_MATCH.match(form['email']) and len(form['email']) > 0:
            messages.error(request, "Invalid Email Address!")
        
        if len(form['password']) > 0 and len(form['password']) < 8 and form['password'] == form['confirm_password']:
            messages.error(request, "Password does not meet the minimum length of 8 characters!")
        
        return redirect('/')
    else:
        data = {'first_name': form['first_name'],
                'last_name': form['last_name'],
                'email': form['email'],
                'password': bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        }
        user = User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])
        request.session['logged_in'] = True
        request.session['user'] = {'user_id':User.objects.get(email=data['email']).id, 'first_name':data['first_name'], 'last_name':data['last_name'], 'email':data['email']}
        messages.info(request, "You successfully registered (or loggined in)!")
        
        return redirect('../success')

def user(request, num=None):
    users = User.objects.filter(id=num)
    if len(users) > 0:
        quotes = Quote.objects.filter(submitter=users[0])
        return render(request, "users/user.html", {'quotes':quotes, 'first_name':users[0].first_name, 'last_name':users[0].last_name, 'email':users[0].email})
    return redirect('../quotes')

def quotes(request):
    quotes = Quote.objects.all()
    return render(request,'users/quotes.html', {'quotes':quotes})

def submit_quote(request):
    if request.method != 'POST':
        return redirect('/quotes')
    
    form = request.POST
    
    if (len(form['author']) < 3) or (len(form['quote']) < 10):
        if len(form['author']) < 3:
            messages.error(request, "The author's name needs to be 3 characters or more")
        if len(form['quote']) < 10:
            messages.error(request, "The quote needs to be 10 characters or more")
        return redirect('/quotes')
    
    submitter = User.objects.get(email=request.session['user']['email'])
    quotes = Quote.objects.create(quote=form['quote'], author=form['author'], submitter=submitter)
    return redirect('/quotes')

def delete_quote(request):
    if request.method != 'POST':
        return redirect('/quotes')
    
    form = request.POST
    Quote.objects.get(id=form['quote_id']).delete()
    return redirect('/quotes')

def edit_user(request):
    if request.method != 'POST':
        return redirect('/quotes')
    
    form = request.POST
    
    errors = {}
    
    user = User.objects.get(id=request.session['user']['user_id'])
    if len(form['first_name']) < 3 or len(form['last_name']) < 3 or ((form['email'] != user.email and len(User.objects.filter(email=form['email'])) > 0) or (not EMAIL_MATCH.match(form['email']))):
        if (form['email'] != user.email and len(User.objects.filter(email=form['email'])) > 0) or (not EMAIL_MATCH.match(form['email'])):
            messages.error(request, "Error cannot change email")
        
        if len(form['first_name']) < 3:
            messages.error(request, "First name cannot be less than three characters")
        if len(form['last_name']) < 3:
            messages.error(request, "Last name cannot be less than three characters")        
        return redirect('/myaccount/{id}'.format(id=user.id))        
    
    
    user.email = form['email']
    user.first_name = form['first_name']
    user.last_name = form['last_name']    
    user.save()
    
    request.session['user'] = {'user_id':user.id, 'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email}
    
    return redirect('/success')

def myaccount(request, num=None):
    if num != request.session['user']['user_id']:
        return redirect('/quotes')
    return render(request, "users/myaccount.html", {})

def likes(request):
    if request.method != 'POST':
        return redirect('/quotes')
    user = User.objects.get(id=request.session['user']['user_id'])
    quote = Quote.objects.get(id=request.POST['quote_id'])
    
    if len(quote.likes.filter(user=user)) == 0:
        Like.objects.create(user=user, quote=quote)
    
    print(Like.objects.filter(quote=quote).count())
    return redirect('/quotes')