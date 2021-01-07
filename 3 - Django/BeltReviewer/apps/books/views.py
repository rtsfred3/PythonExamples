from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

import re
import bcrypt

from apps.users.models import *
from apps.books.models import *

NAME_MATCH = re.compile(r'.[^1-9\s]*')
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    reviews = Review.objects.all().order_by('-id')[:3]
    books = Book.objects.all()
    return render(request,'books/index.html', {'reviews':reviews, 'books':books})

def book(request, num=None):
    books = Book.objects.filter(id=num)
    if len(books) > 0:
        return render(request, "books/book.html", {'book':books[0], 'reviews':Review.objects.filter(book=books[0])})
    return redirect('/books')

def create(request):
    if request.method != 'POST' or not request.session['logged_in']:
        return redirect('/books')
    
    form = request.POST
    
    author = form['author-text']
    if form['author-text'] == "":
        author = form['author-list']
    
    if Book.objects.filter(title=form['title']):
        return redirect('/books/'+str(Book.objects.filter(title=form['title'])[0].id))    
        
    if len(Author.objects.filter(name=author)) == 0:
        author = Author.objects.create(name=author)
    
    #author = Author.objects.last()
    uploader = User.objects.get(email=request.session['user']['email'])
    book = Book.objects.create(title=form['title'], author=author, uploader=uploader)
    
    Review.objects.create(rating=int(form['rating']), review=form['review'], reviewer=uploader, book=book)
    return redirect('/books/'+str(book.id))

def add(request):
    authors = Author.objects.all()
    return render(request, "books/add.html", {'authors':authors})