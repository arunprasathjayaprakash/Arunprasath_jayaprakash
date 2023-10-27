from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = {
        'Name' : 'Arun prasath jayaprakash',
        'Email': 'arun826.jp@gmail.com',
        'Project' : 'Django'
    }

    return render(request , 'base.html' ,context=content)

def home(request):
    return HttpResponse("<h1>home from pycharm</h2>")