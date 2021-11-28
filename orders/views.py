from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .forms import CreateUserForm
from .models import *
from django.urls import reverse
from datetime import datetime
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

    estado = Estado.objects.get(id=1)
    user = User.objects.get(id=request.user.id)
    header = Orden.objects.filter(estado=estado, idUsuario=user)
    items = DetalleOrden.filter(idOrden=header)
    context = {
        'Opciones': OpcionMenu.objects.all(),
        'Toppings': Toppings.objects.all(),
        'header': header,
        'items': items
    }   

    opcion = {}
    if request.method == 'POST':
        orders = Orden.objects.filter(idUSuario=request.user.id)
        
        opcion = request.POST['opcionesMenu']
        topping = request.POST.getlist('topping')
        cantidad = request.POST['cantidad']

        precio = OpcionMenu.objects.get(id=opcion)
        subtotal = precio.precio * int(cantidad)
        
        print("---------------------")
        
        if not orders.exists():
            currentOrden = Orden(total=0, fecha=datetime.now(), idUSuario=user, estado=Estado.objects.get(id=1))
            currentOrden.save()

            request.session['currentOrder'] = currentOrden.id;

        exist = False
        for order in orders:
            if order.estado.id == 1:
                exist = True
                break
            else:
                exist = False


        if exist:
            print("------------")
            print("SUCCESS")
            currentOrden = Orden.objects.get(id = request.session['currentOrder'])
                
        else:

            currentOrden = Orden(total=0, fecha=datetime.now(), idUSuario=user, estado=Estado.objects.get(id=1))
            currentOrden.save()

            request.session['currentOrder'] = currentOrden.id;
                
        print(request.session['currentOrder'])
        detalle = DetalleOrden(idOrden = currentOrden, idOpcion=precio, cantidad=cantidad, subtotal=subtotal)
        detalle.save()

        for item in topping:
            top = Toppings.objects.get(id=item)

            detalleTopping = DetalleOrdenTopping(idDetalleOrden= detalle, idTopping=top)
            detalleTopping.save()

        return render(request, 'accounts/index.html', context)

    else:
        
        return render(request, 'accounts/index.html', context)

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