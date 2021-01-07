from django.shortcuts import render, HttpResponse, redirect

import datetime

def index(request):
    if not ('messages' in request.session):
        request.session['messages'] = []
    colors = [{'id':'red', 'name':'Red'},
              {'id':'blue', 'name':'Blue'},
              {'id':'green', 'name':'Green'},
              {'id':'black', 'name':'Black'},
              ]
    
    colors_dict = {color['id']:color['name'] for color in colors}
    
    return render(request, 'SessionWords/index.html', {'colors':colors})

def process(request):
    if request.method == 'POST':
        form = request.POST
        font = '24pt' if len(form.getlist('big')) != 0 and form.getlist('big')[0] == 'on' else '12pt'
        
        temp = request.session['messages']
        temp.append({'message':form['message'], 'color':form['color'], 'font':font, 'date':' - added at '+'{0:%H:%M:%S %p, %b %dth %Y}'.format(datetime.datetime.now())})
        request.session['messages'] = temp
        
        return redirect('/session_words/')
    return redirect('/session_words/')

def destroy(request):
    if request.method == 'POST':
        request.session['messages'] = []
        return redirect('/session_words/')
    return redirect('/session_words/')