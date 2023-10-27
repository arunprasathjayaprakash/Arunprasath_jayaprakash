from django.urls import path
from .views import home , index

urlpatterns = [
    path('', index , name='website_home'),
]
