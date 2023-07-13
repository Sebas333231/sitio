from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from ventas.models import VentasAptos, Visita
from django.forms import modelform_factory

# Create your views here.
def pagina(request):
    no_ventas_var = VentasAptos.objects.count()
    ventas = VentasAptos.objects.all()
    return render(request, 'index.html', {'no_ventas': no_ventas_var, 'ventas':ventas})


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login.html')
    template_name = 'registration/signup.html'



def bienvenidos(request):
    no_ventas_var = VentasAptos.objects.count()
    ventas = VentasAptos.objects.all()
    return render(request, 'ventas.html', {'no_ventas': no_ventas_var, 'ventas':ventas})


def casa(request):
    no_ventas_var = VentasAptos.objects.count()
    ventas = VentasAptos.objects.all()
    return render(request, 'index.html', {'no_ventas': no_ventas_var, 'ventas':ventas})


def cards(request):
    numero_aptos = VentasAptos.objects.count()
    aptos = VentasAptos.objects.all()
    return render(request, 'cards.html', {'numero_ap': numero_aptos, 'cards': aptos})

def detalleVenta(request, id):
    venta = VentasAptos.objects.get(pk=id)
    return render(request, 'detalle.html', {'card': venta})

VentaForm = modelform_factory(VentasAptos, exclude=[])

def nuevaVenta(request):
    if request.method == 'POST':
        formaVenta = VentaForm(request.POST)
        if formaVenta.is_valid():
            formaVenta.save()
            return redirect('hola')
    else:
        formaVenta = VentaForm()
    return render(request, 'nuevo.html', {'formaVenta': formaVenta})

def editarventa(request, id):
    venta = get_object_or_404(VentasAptos, pk=id)
    if request.method == 'POST':
        formaVenta = VentaForm(request.POST, instance=venta)
        if formaVenta.is_valid():
            formaVenta.save()
            return redirect('hola')
    else:
        formaVenta = VentaForm(instance=venta)
    return render(request, 'editar.html', {'formaVenta': formaVenta})

def eliminar(request, id):
    venta = get_object_or_404(VentasAptos, pk=id)
    venta.delete()
    return redirect('hola')


#funciones de las visitas
def bienvenidos_dos(request):
    no_visitas_var = Visita.objects.count()
    visita = Visita.objects.all()
    return render(request, 'visitas.html', {'no_visitas': no_visitas_var, 'visitas':visita})

def detalleVisita(request, id):
    visita = Visita.objects.get(pk=id)
    return render(request, 'detalle_visita.html', {'visita': visita})

VisitaFrom = modelform_factory(Visita, exclude=[])

def nuevaVisita(request):
    if request.method == 'POST':
        formaVisita = VisitaFrom(request.POST)
        if formaVisita.is_valid():
            formaVisita.save()
            return redirect('informacion')
    else:
        formaVisita = VisitaFrom()
    return render(request, 'nueva_visita.html', {'formaVisita': formaVisita})

def editarVisita(request, id):
    venta = get_object_or_404(Visita, pk=id)
    if request.method == 'POST':
        formaVisita = VisitaFrom(request.POST, instance=venta)
        if formaVisita.is_valid():
            formaVisita.save()
            return redirect('visita')
    else:
        formaVisita = VisitaFrom(instance=venta)
    return render(request, 'editar_visita.html', {'formaVisita': formaVisita})

def eliminar_visita(request, id):
    venta = get_object_or_404(Visita, pk=id)
    venta.delete()
    return redirect('visita')
