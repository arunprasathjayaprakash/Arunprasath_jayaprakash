from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import FormFields , Contacts

def index(request):

    content = {
     'value':[val for val in  Contacts.objects.all().values()]
    }


    # return render(request , 'base.html' , {'render':content})
    return render(request , 'base_test.html' , {'render':content})

def form_fields():
    pass


def create_contact(request):
    # return render(request,'test_template.html')
    return render(request, 'create_page.html')

def record_data(request):
    if request.method == 'POST':
        form = FormFields(request.POST)
        if form.is_valid():
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