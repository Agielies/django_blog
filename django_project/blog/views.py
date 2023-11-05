
from django.http import HttpResponse

def home(request):

    return HttpResponse('Home page for blog')

def about(request):

    return HttpResponse('<h1> This is the about page </h1>')