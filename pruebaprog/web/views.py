from django.shortcuts import render, redirect, get_object_or_404
from .models import Obras , Contacto
from .forms import ContactoForm, ObrasForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from web.Carrito import Carrito
from web.models import Obras
from decimal import Decimal
# Create your views here.

def home(request):
    return render(request, 'web/home.html')

def pagina02(request):
    return render(request, 'web/pagina02.html')

def pagina03(request):
    return render(request, 'web/pagina03.html')

def pagina04(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
        messages.success(request,"Datos Guardados;)")
    return render(request, 'web/pagina04.html', data)




def pagina05(request):
    return render(request, 'web/pagina05.html')

def pagina06(request):
    return render(request, 'web/pagina06.html')

def pagina07(request):
    obras = Obras.objects.all()
    data = {
        'obras': obras
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario


    return render(request, 'web/pagina07.html',{'obras':obras})

def agregar_obras(request, obras_id):
    carrito = Carrito(request)
    obras = Obras.objects.get(id=obras_id)
    carrito.agregar(obras)
    return redirect("pagina07")

def eliminar_obras(request, obras_id):
    carrito = Carrito(request)
    obras = Obras.objects.get(id=obras_id)
    carrito.eliminar(obras)
    return redirect("pagina07")

def restart_obras(request, obras_id):
    carrito = Carrito(request)
    obras = Obras.objects.get(id=obras_id)
    carrito.restart(obras)
    return redirect("pagina07")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("pagina07")

@permission_required('app.add_obra')
def agregar_producto(request):
    data = {
        'form': ObrasForm()
    }

    if request.method == 'POST':
        formulario = ObrasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'web/productos/agregar.html', data)

@permission_required('app.view_obra')
def listar_producto(request):
    productos = Obras.objects.all()

    data = {
        'productos': productos
    }
    
    return render(request, 'web/productos/listar.html', data)

@permission_required('app.change_obras')
def modificar_producto(request, id):
    
    producto = get_object_or_404(Obras, id=id)

    data = {
        'form': ObrasForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ObrasForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request, 'web/productos/modificar.html', data)

@permission_required('app.delete_obras')
def eliminar_producto(request, id):
    producto = get_object_or_404(Obras, id=id)
    producto.delete()
    return redirect(to="listar_producto")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)