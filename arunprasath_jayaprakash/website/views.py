from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import FormFields , Contacts

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
            if not Contacts.objects.filter(name=name,email=email).exists():
                contact_add = Contacts(name=name, email=email)
                contact_add.save()
                return render(request, 'create_page.html',{'form':form,'message':'Created Successfully'})
            else:
                return render(request, 'create_page.html', {'form': form, 'message': 'Contact Already Exists in Database'})
    else:
        form = FormFields()
    return render(request, 'create_page.html',{'form':form})


def home(request):
    return HttpResponse("<h1>home from pycharm</h2>")