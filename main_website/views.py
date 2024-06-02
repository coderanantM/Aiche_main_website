from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return HttpResponse('<h1>About page</h1>')

def index(request):
    return HttpResponse(request, 'main_website/index.html')

def blog(request):
    return HttpResponse(request, 'main_website/blog.html')

def contact(request):
    return HttpResponse(request, 'main_website/contact.html')

def events(request):
    return HttpResponse(request, 'main_website/events.html')

def team(request):
    return HttpResponse(request, 'main_website/team.html')