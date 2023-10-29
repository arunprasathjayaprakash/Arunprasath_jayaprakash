from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import FormFields
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
    return render(request,'test_template.html')

def record_data(request):
    # if request.method == 'POST':  # If the form has been submitted...
    #     form = FormFields(request.POST)  # A form bound to the POST data
    #     # if form.is_valid():  # All validation rules pass
    #         # Process the data in form.cleaned_data
    #         # ...
    #
    #     name = form['name']
    #     email = form['email']
    #     return HttpResponseRedirect('/thanks/')
            # Redirect after POST
    # return render(request,'new_contact_page.html')
    return render(request, 'test_template.html')

def home(request):
    return HttpResponse("<h1>home from pycharm</h2>")