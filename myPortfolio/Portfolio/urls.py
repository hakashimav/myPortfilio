
from django.contrib import admin
from django.urls import path,include
#from django.conf.urls import url, handler404
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('realisation',views.realisation,name='realisation'),
    path('contact',views.contact,name='contact'),
]