from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = {
        'Name' : 'Arun prasath jayaprakash',
        'Email': 'arun826.jp@gmail.com',
        'Project' : 'Django'
    }

    return render(request , 'base.html' , {'render':content})

def create_contact(request):
    return render(request,'new_contact_page.html')

def home(request):
    return HttpResponse("<h1>home from pycharm</h2>")