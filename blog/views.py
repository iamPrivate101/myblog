from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    { 
        'author':'sameer',
        'title' : 'blog 1',
        'content': 'first post',
        'date_posted' : 'aug 4 2342'
    },
    { 
        'author':'reemas',
        'title' : 'blog 2',
        'content': 'second post',
        'date_posted' : 'aug 5 2342'
    }
]

def home(request):
    context = {
        'posts' : posts,
        'title':'Home',

    }
    return render(request, 'blog/home.html',context)

def about(request):
    context = {
        'title':'About',
    }
    return render(request, 'blog/about.html', context)
