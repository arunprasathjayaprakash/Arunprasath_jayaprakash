from django.shortcuts import render
from .forms import FormFields , Contacts , UpdateForm , DeleteForm

def index(request,message=False,update=True):
    columns = ['id','name','email','created_time']
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
    if message:
        if update:
            return render(request, 'base_template_working.html', {'render': content,'message': 'Contact Updated Successfully'})
        else:
            return render(request, 'base_template_working.html',
                          {'render': content, 'message': 'Contact deleted Successfully'})
    return render(request , 'base_template_working.html' , {'render':content})

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

def edit_record(request,id,id_1='False'):
    record = Contacts.objects.get(id=id)
    record_list = [record.id,record.name, record.email, record.created_time]
    if id_1=='True':
        form_data = {'id':record_list[0],'name':record_list[1],'email':record_list[2],'created_time':record_list[3]}
        update_form = UpdateForm(initial=form_data)
        return render(request, 'update_page.html', {'record': update_form})
    return render(request, 'edit_page.html',{'record':record_list})

def update_record(request,id):
    if request.method == 'POST':
        form = FormFields(request.POST)
        if form.is_valid():
            db = Contacts.objects.get(id=id)
            if db.name != form.cleaned_data['name'] or db.email != form.cleaned_data['email']:
                db.name = form.cleaned_data['name']
                db.email = form.cleaned_data['email']
                db.save()
                return index(request,message=True,update=True)
            else:
                record = Contacts.objects.get(id=id)
                record_list = [record.id, record.name, record.email, record.created_time]
                form_data = {'id': record_list[0], 'name': record_list[1], 'email': record_list[2],
                             'created_time': record_list[3]}
                update_form = UpdateForm(initial=form_data)
                return render(request, 'update_page.html', {'record': update_form, 'message': 'No New Information to update'})


def delete_confirmation(request,id):
    db = Contacts.objects.get(id=id)
    record_list = [db.id, db.name, db.email, db.created_time]
    form_data = {'id': record_list[0], 'name': record_list[1], 'email': record_list[2],
                 'created_time': record_list[3]}
    update_form = DeleteForm(initial=form_data)
    return render(request, 'delete_page.html', {'record': update_form})

def delete_record(request,id):
    db = Contacts.objects.get(id=id)
    db.delete()
    return index(request,message=True,update=False)