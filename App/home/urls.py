import imp
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('store', views.store, name='store'),
    path('pricing', views.pricing, name='pricing'),
    path('contact', views.contact, name='contact'),
]