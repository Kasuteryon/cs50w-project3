from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .forms import CreateUserForm
from .models import *
from django.urls import reverse
# Create your views here.



def index(request):

    context = {
        'Regular': OpcionMenu.objects.filter(idCategoria__exact=1).order_by('-contador'),
        'Siciliana': OpcionMenu.objects.filter(idCategoria__exact=2).order_by('-contador'),
        'Subs': OpcionMenu.objects.filter(idCategoria__exact=3).order_by('-contador'),
        'Ensaladas': OpcionMenu.objects.filter(idCategoria__exact=4).order_by('-contador'),
        'Pasta': OpcionMenu.objects.filter(idCategoria__exact=5).order_by('-contador'),
        'Cena': OpcionMenu.objects.filter(idCategoria__exact=6).order_by('-contador')
        
    }

    return render(request, 'orders/index.html', context)


def my_profile(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'accounts/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)