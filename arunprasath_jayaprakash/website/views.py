from django.shortcuts import render
from .forms import FormFields , Contacts , UpdateForm , DeleteForm

def index(request,message=False,update=False,delete=False):
    '''
    Return main page rendered with information for the user

    :param request: incoming request
    :param message: returns alert message if True
    :param update: transfers to update flow if True
    :param delete: transfers to delete flow if True

    '''
    columns = ['id','name','email','created_time']
    formatted_value = []

    for val in Contacts.objects.all().values():
        temp = []
        for k, v in val.items():
            if k in columns:
                temp.append(v)
        formatted_value.append(temp)

    #form content to be posted in the main page
    content = {
     'value':formatted_value
    }

    if message:
        if update:
            return render(request, 'base.html', {'render': content,'message': 'Contact Updated Successfully'})
        elif delete:
            return render(request, 'base.html',
                          {'render': content, 'message': 'Contact deleted Successfully'})
        else:
            return render(request, 'base.html',
                          {'render': content, 'message': 'Contact Created Successfully'})

    return render(request , 'base.html' , {'render':content})

def create_contact(request):
    '''
    Renders form for creating contact

    :param request:
    :return: contact fields required
    '''
    form = FormFields()
    return render(request, 'create_page.html',{'form':form})

def record_data(request):
    '''
    Adds data to DB when requested returns alert message

    :param request: valid POST request
    :return: render Success if True
    '''
    if request.method == 'POST':
        form = FormFields(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            if not Contacts.objects.filter(name=name).exists() and not Contacts.objects.filter(email=email).exists():
                contact_add = Contacts(name=name, email=email)
                contact_add.save()
                return index(request,message=True)
            else:
                return render(request, 'create_page.html', {'form': form, 'message': 'Name or email'
                                                                                     ' Already Exists in Database'})
    else:
        form = FormFields()
    return render(request, 'create_page.html',{'form':form})

def edit_record(request,id,id_1='False'):
    '''
    Edits record from update page if request is valid

    :param request: Incoming request
    :param id: Id for the record to be retrived
    :param id_1:
    :return: Returns True if Success
    '''
    record = Contacts.objects.get(id=id)
    record_list = [record.id,record.name, record.email, record.created_time]
    if id_1=='True':
        form_data = {'id':record_list[0],'name':record_list[1],'email':record_list[2],'created_time':record_list[3]}
        update_form = UpdateForm(initial=form_data)
        return render(request, 'update_page.html', {'record': update_form})
    return render(request, 'edit_page.html',{'record':record_list})

def update_record(request,id):
    '''
    Returns updated message with valid request

    :param request: request
    :param id: id for data to be updated
    :return: Return Success if request is valid
    '''
    if request.method == 'POST':
        form = FormFields(request.POST)
        if form.is_valid():
            db = Contacts.objects.get(id=id)
            if db.name != form.cleaned_data['name'] or db.email != form.cleaned_data['email']:
                if not Contacts.objects.filter(name=form.cleaned_data['name']).exists() or  not Contacts.objects.filter(
                        email=form.cleaned_data['email']).exists():
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
                    return render(request, 'update_page.html',
                                  {'record': update_form, 'message': 'Data Exists in the database as a seperate entry'})

            else:
                record = Contacts.objects.get(id=id)
                record_list = [record.id, record.name, record.email, record.created_time]
                form_data = {'id': record_list[0], 'name': record_list[1], 'email': record_list[2],
                             'created_time': record_list[3]}
                update_form = UpdateForm(initial=form_data)
                return render(request, 'update_page.html', {'record': update_form, 'message': 'No New Information to update'})


def delete_confirmation(request,id):
    '''
    Transfers to delete page after confirmation

    :param request: valid Request for deleting request
    :param id: id of the record to be deleted
    :return: Success if valid
    '''
    db = Contacts.objects.get(id=id)
    record_list = [db.id, db.name, db.email, db.created_time]
    form_data = {'id': record_list[0], 'name': record_list[1], 'email': record_list[2],
                 'created_time': record_list[3]}
    update_form = DeleteForm(initial=form_data)
    return render(request, 'delete_page.html', {'record': update_form})

def delete_record(request,id):
    '''
    Deletes record from DB

    :param request: valid request for deletion
    :param id: id for deleting record
    :return: transfers to index with message if success
    '''
    db = Contacts.objects.get(id=id)
    db.delete()
    return index(request,message=True,delete=True)