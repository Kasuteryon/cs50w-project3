from django.urls import path
from django.contrib import admin
from django.urls import include, path
#from .views import *
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.my_profile, name='profile'),
    path('register/', views.register, name='register'),
    path('history/', views.history, name='history'),
    path('jet/', include('jet.urls', 'jet')),
    
]
