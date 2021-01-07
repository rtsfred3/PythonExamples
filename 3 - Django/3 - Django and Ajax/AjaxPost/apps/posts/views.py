from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import serializers

from .models import *

# Create your views here.
def index(request):
    return render(request, 'posts/index.html', {})

def all_json(request):
    posts = Post.objects.all()
    return HttpResponse(serializers.serialize("json", posts), content_type='application/json')

def create(request):
    if request.method == 'POST':
        Post.objects.create(post=request.POST['post'])
    return all_json(request)