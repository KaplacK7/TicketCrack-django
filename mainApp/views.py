from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .serializers import EventosSerializer, VentasSerializer
from mainApp.models import Funcion, Eventos, Ventas, Ubicacion, Categoria
from mainApp.forms import FormVenta
import datetime 

# Constantes
DESCUENTO = 10  # Porcentaje
MIN_ENTRADAS_DESCUENTO = 3

# =====================
# API Views
# =====================

class EventosList(generics.ListCreateAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer

class EventosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer

class VentasList(generics.ListAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

# =====================
# Vistas HTML (solo backend)
# =====================

def index(request):
    funciones = Funcion.objects.all()
    return render(request, 'index.html', {'funciones': funciones})

def ticket(request, id):
    venta = get_object_or_404(Ventas, id=id)
    return render(request, 'ticket.html', {'venta': venta})

def comprar(request, id):
    funcion = get_object_or_404(Funcion, id=id)
    form = FormVenta(initial={'id_funcion': id}, funcion_id=id)

    if request.method == 'POST':
        form = FormVenta(request.POST, funcion_id=id)
        if form.is_valid():
            cantidad = form.cleaned_data['entradas']
            ubicacion = form.cleaned_data['ubicacion']

            disponibles = ubicacion.asientos_disponibles - ubicacion.asientos_vendidos
            if cantidad > disponibles:
                form.add_error('entradas', 'No hay suficientes entradas para esta ubicación.')
            else:
                venta = Ventas()
                venta.funcion = funcion
                venta.cliente = form.cleaned_data['cliente']
                venta.email = form.cleaned_data['email']
                venta.entradas = cantidad
                venta.fecha = datetime.datetime.now()

                codigo = form.cleaned_data.get('codigo', '')
                venta.codigo = codigo if codigo else None

                # Calcular descuento
                descuento = DESCUENTO if cantidad >= MIN_ENTRADAS_DESCUENTO and codigo else 0

                # Calcular totales
                valor_entrada = ubicacion.precio
                total_original = cantidad * valor_entrada
                total_descuento = total_original * descuento / 100
                total_final = total_original - total_descuento

                venta.total_original = total_original
                venta.total_descuento = total_descuento
                venta.total_final = total_final
                venta.ubicacion = ubicacion
                venta.save()

                # Actualizar asientos vendidos
                ubicacion.asientos_vendidos += cantidad
                ubicacion.save()

                return redirect('/ticket/' + str(venta.id))

    return render(request, 'comprar.html', {
        'funcion': funcion,      
        'form': form,
    })




def eventos_por_categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    funciones = Funcion.objects.filter(evento__categorias=categoria)

    # Renderizar plantilla HTML específica por categoría
    template_map = {
        'musica': 'musica.html',
        'deportes': 'deportes.html',
        'teatro': 'teatro.html',
    }

    template_name = template_map.get(categoria_slug, 'index.html')

    return render(request, template_name, {
        'categoria': categoria,
        'funciones': funciones
    })