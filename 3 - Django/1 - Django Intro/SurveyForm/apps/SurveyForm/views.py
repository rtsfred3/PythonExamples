from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

locations = [{'id':'san_jose','name':'San Jose'},
             {'id':'seattle','name':'Seattle'},
             {'id':'los_angeles','name':'Los Angeles'},
             {'id':'dallas','name':'Dallas'},
             {'id':'tysons_corner','name':'Tysons Corner'},
             {'id':'chicago','name':'Chicago'},
             {'id':'tulsa','name':'Tulsa'},
             {'id':'east_bay','name':'East Bay'}]

languages = [{'id':'java','name':'Java'},
             {'id':'javascript','name':'Javascript'},
             {'id':'python','name':'Python'},
             {'id':'php','name':'PHP'},
             {'id':'ruby','name':'Ruby'},
             {'id':'c++','name':'C++'},
             {'id':'c','name':'C'},
             {'id':'c#','name':'C#'}]

languages_dict = {language['id']:language['name'] for language in languages}
locations_dict = {location['id']:location['name'] for location in locations}

def index(request):
    global locations
    global languages
        
    return render(request, 'SurveyForm/index.html', {'languages':languages, 'locations':locations})

def process(request):
    global languages_dict
    global locations_dict
    if request.method == 'POST':
        form = request.POST
        print(form['name'])
        request.session['user'] = {'name':form['name'], 'location':locations_dict[form['location']], 'language':languages_dict[form['language']], 'comment':form['comments']}
        
        return redirect('../result')
    return redirect('..')

def result(request):
    return render(request, 'SurveyForm/result.html')