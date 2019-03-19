from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_url_address, name='get_url_address')
]
