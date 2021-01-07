from django.http import HttpResponse

def surveyindex(request):
    return HttpResponse("placeholder to display all the surveys created")

def surveynew(request):
    return HttpResponse("placeholder for users to add a new survey")