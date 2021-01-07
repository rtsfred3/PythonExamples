from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime
import os, time, datetime


def index(request):
    x = datetime.datetime.now()
    context = { "time": strftime("%Y-%m-%d %H:%M:%S %p", x.timetuple()) }
    return render(request,'DisplayTime/index.html', context)