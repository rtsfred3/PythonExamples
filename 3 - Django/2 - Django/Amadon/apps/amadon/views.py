from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

items = [{'id':0, 'name':'Dojo Tshirt', 'price':19.99, 'quantity':15},
         {'id':1, 'name':'Dojo Sweater', 'price':29.99, 'quantity':15},
         {'id':2, 'name':'Dojo Cup', 'price':4.99, 'quantity':15},
         {'id':3, 'name':'Algorithm Book', 'price':49.99, 'quantity':10}]

for item in items: item['quantity']+=1

itemsDict = {item['id']:item for item in items}

# Create your views here.
def index(request):
    global items
    global itemsDict
    if not ('spent' in request.session): request.session['spent'] = 0
    if not ('total_spent' in request.session): request.session['total_spent'] = 0
    if not ('items_bought' in request.session): request.session['items_bought'] = 0
    return render(request, 'amadon/index.html', {'items':items})

def buy(request):
    global items
    if request.method == 'POST':
        form = request.POST
        temp_spent = 0
        temp_bought = 0
        for item in items:
            temp_spent += item['price']*int(form['quantity_'+str(item['id'])])
            temp_bought += int(form['quantity_'+str(item['id'])])
        request.session['spent'] = request.session['spent']+temp_spent
        request.session['total_spent'] = request.session['total_spent']+temp_spent
        request.session['items_bought'] = request.session['items_bought']+temp_bought
    return redirect('checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html', {})