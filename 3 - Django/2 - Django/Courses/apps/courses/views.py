from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
if not Course.objects.filter(name="Physics").exists():
    Course.objects.create(name="Physics", description="Physics")

# Create your views here.
def index(request):
    return render(request, 'courses/index.html', {'courses':Course.objects.all()})

def create(request):
    if request.method == 'POST':
        form = request.POST
        name, description = form['name'], form['description']
        if len(name) < 5 or len(description) < 15:
            if len(name) < 5:
                #messages.add_message(request, messages.INFO, 'Name is less than 5 characters')
                messages.info(request, 'Name is less than 5 characters')
            if len(description) < 15:
                #messages.add_message(request, messages.INFO, 'Description is less than 15 characters')
                messages.info(request, 'Description is less than 15 characters')
            return redirect('../')
        Course.objects.create(name=name, description=description)
    return redirect('../')

def destroy(request, num=None):
    return render(request, 'courses/destroy.html', {'course':Course.objects.get(id=num)})

def destroy_course(request):
    if request.method == 'POST':
        form = request.POST    
        Course.objects.get(id=form['id']).delete()
    return redirect('../')