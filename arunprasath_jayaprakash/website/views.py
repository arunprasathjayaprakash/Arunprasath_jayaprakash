from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import FormFields
from django.contrib import messages
from django import forms

def index(request):
    content = {
        'Name' : 'Arun prasath jayaprakash',
        'Email': 'arun826.jp@gmail.com',
        'Project' : 'Django'
    }

    return render(request , 'base.html' , {'render':content})

def form_fields():
    pass


def create_contact(request):
    # return render(request,'test_template.html')
    return render(request, 'create_page.html')

def record_data(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = FormFields(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'create_page.html',{'form':form,'message':'Created Successfully'})
    else:
        form = FormFields()
    return render(request, 'create_page.html',{'form':form})

def home(request):
    return HttpResponse("<h1>home from pycharm</h2>")