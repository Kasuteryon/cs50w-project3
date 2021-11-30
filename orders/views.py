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
    user = User.objects.get(id=request.user.id)
    
    if request.method == 'POST':
        orders = Orden.objects.filter(idUSuario=request.user.id)
        
        opcion = request.POST['opcionesMenu']
        topping = request.POST.getlist('topping')
        cantidad = request.POST['cantidad']

        precio = OpcionMenu.objects.get(id=opcion)
        subtotal = precio.precio * int(cantidad)
    
        
        if not orders.exists():
            currentOrden = Orden(total=0, fecha=datetime.now(), idUSuario=user, estado=Estado.objects.get(id=1))
            currentOrden.save()

            # request.session['currentOrder'] = currentOrden.id;
            
            
            try:
                # orderExists = CurrentOrder.objects.get(idOrden=currentOrden.id, idUser=request.user.id)
                current = CurrentOrder.objects.get(idUser=request.user.id)
                current.idOrden = currentOrden
                current.save()
            except:
                current = CurrentOrder(idOrden=currentOrden, idUser=request.user)
                current.save()
                

        exist = False
        for order in orders:
            if order.estado.id == 1:
                exist = True
                break
            else:
                exist = False


        if exist:
            #print("------------")
            #print("SUCCESS")
            current = CurrentOrder.objects.filter(idUser=request.user.id)
            #print(current[0].idOrden.id)
            od = Orden.objects.get(id=current[0].idOrden.id)
            currentOrden = Orden.objects.get(id = od.id)

            
                
        else:

            currentOrden = Orden(total=0, fecha=datetime.now(), idUSuario=user, estado=Estado.objects.get(id=1))
            currentOrden.save()
            print("---------------------")
            #print(currentOrden.id)
            current = CurrentOrder.objects.get(idUser=user.id)
            #equest.session['currentOrder'] = currentOrden.id;
            #print(current[0])
            current.idOrden = currentOrden
            current.save()
                
        # print(request.session['currentOrder'])
        detalle = DetalleOrden(idOrden = currentOrden, idOpcion=precio, cantidad=cantidad, subtotal=subtotal)
        detalle.save()

        currentOrden.total += subtotal
        currentOrden.save()

        for item in topping:
            top = Toppings.objects.get(id=item)

            detalleTopping = DetalleOrdenTopping(idDetalleOrden= detalle, idTopping=top)
            detalleTopping.save()

        return HttpResponseRedirect(reverse('profile'))

    else:

        estado = Estado.objects.get(id=1)
        
        header = Orden.objects.filter(estado=estado, idUSuario=user)
        

        try:
            items = DetalleOrden.objects.filter(idOrden=header[0])
        except IndexError:
            items = ''
        context = {
            'Opciones': OpcionMenu.objects.all(),
            'Toppings': Toppings.objects.all(),
            'header': header,
            'items': items
        }   
        print("---------------------")
        print(items)

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