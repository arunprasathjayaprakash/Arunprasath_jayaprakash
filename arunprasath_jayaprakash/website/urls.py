from django.urls import path
from .views import home , index , create_contact

urlpatterns = [
    path('', index , name='website_home'),
    path('create',create_contact , name='create_contact_page' )
]
