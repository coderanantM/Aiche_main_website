from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, 'templates/base.html')

def blog(request):
    return render(request, 'templates/blog.html')

def contact(request):
    return render(request, 'templates/contact.html')

def events(request):
    return render(request, 'templates/events.html')

def team(request):
    return render(request, 'templates/team.html')