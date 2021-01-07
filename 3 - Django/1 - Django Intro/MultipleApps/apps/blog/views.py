from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def blogindex(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def blognew(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def blogcreate(request):
    return HttpResponseRedirect('/')

def blogview(request, num=None):
    return HttpResponse("placeholder to display blog %d" % (num))

def blogedit(request, num=None):
    return HttpResponse("placeholder to edit blog %d" % (num))

def blogdelete(request, num=None):
    return HttpResponseRedirect('/')