from django.shortcuts import render
from .models import Obras
from .forms import ContactoForm

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


    return render(request, 'web/pagina07.html', data)