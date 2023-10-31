from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import FormFields , Contacts

def index(request):
    columns = ['name','email','created_time']
    formatted_value = []

    for val in Contacts.objects.all().values():
        temp = []
        for k, v in val.items():
            if k in columns:
                temp.append(v)
        formatted_value.append(temp)
    content = {
     'value':formatted_value
    }

    # return render(request , 'base.html' , {'render':content})
    return render(request , 'base_template_working.html' , {'render':content})

def form_fields():
    pass


def create_contact(request):
    # return render(request,'test_template.html')
    form = FormFields()
    return render(request, 'create_page.html',{'form':form})

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