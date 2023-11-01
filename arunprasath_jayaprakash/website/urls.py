from django.urls import path
from .views import index , create_contact , record_data ,edit_record , update_record

urlpatterns = [
    path('', index , name='website_home'),
    path('create',create_contact , name='create_contact_page' ),
    path('data_value',record_data , name="record"),
    path('edit/<id>/',edit_record,name='edit_value'),
    path('update/<id>/<id_1>/',edit_record,name='update_value'),
    path('complete',update_record,name='complete_update')
]
