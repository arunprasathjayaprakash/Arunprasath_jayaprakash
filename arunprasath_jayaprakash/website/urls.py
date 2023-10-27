from django.urls import path
from .views import home , index , create_contact , record_data

urlpatterns = [
    path('', index , name='website_home'),
    path('create',create_contact , name='create_contact_page' ),
    path('data_value',record_data , name="record")
]
