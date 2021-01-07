from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not ('word' in request.session):
        return redirect('reset')
    if not ('count' in request.session):
        request.session['count'] = 0
        
    return render(request,'RandomWord/index.html')

def reset(request):
    if 'count' in request.session:
        request.session['count'] += 1    
    request.session['word'] = get_random_string(length=14)
    return redirect('..')