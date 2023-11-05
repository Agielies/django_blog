from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'MichaeM',
        'title' : 'Blog post 1',
        'content' : 'First post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'Corey',
        'title' : 'Blog post 2',
        'content' : 'First post content',
        'date_posted' : 'August 27, 2018'
    },
]

def home(request):

    context = {
        'posts' : posts,
        'title' : 'Michael',
    }
    return render(request,'blog/home.html',context) 

def about(request):

    return render(request, 'blog/about.html') 