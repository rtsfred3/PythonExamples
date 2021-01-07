from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def index(request):
    return HttpResponse("placeholder to later display all the list of blogs.")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog.")

def create(request):
    return HttpResponseRedirect('/')

def year(request, year=None):
    return HttpResponse("placeholder to display blog %d" % (year))

def yearedit(request, year=None):
    return HttpResponse("placeholder to edit blog %d" % (year))

def yeardelete(request, year=None):
    return HttpResponseRedirect('/')