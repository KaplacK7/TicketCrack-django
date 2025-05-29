from django.contrib import admin
from mainApp.models import Eventos, Funcion, Ventas, Ubicacion, Categoria

# Inline para mostrar los eventos dentro de la categoría
class EventoInline(admin.TabularInline):
    model = Categoria.eventos.through  # tabla intermedia de ManyToMany
    extra = 1

# Admin de Categoría mejorado para soportar múltiples eventos
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [EventoInline]
    exclude = ('eventos',)  # para evitar mostrar dos veces el campo

# Admin del modelo Eventos (sin cambios mayores)
class EventoForm(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'productora', 'mostrar_categorias']

    def mostrar_categorias(self, obj):
        return ", ".join([cat.nombre for cat in obj.categorias.all()])
    mostrar_categorias.short_description = 'Categorías'

# Otros modelos como los tienes
class FuncionForm(admin.ModelAdmin):
    list_display = ['evento', 'fecha', 'hora', 'asientos_vendidos', 'lugar']

class VentasForm(admin.ModelAdmin):
    list_display = ['funcion', 'cliente', 'entradas', 'total_original', 'total_final']

class UbicacionForm(admin.ModelAdmin):
    list_display = ['funcion', 'nombre', 'precio', 'asientos_disponibles']

# Registro de modelos
admin.site.register(Eventos, EventoForm)
admin.site.register(Funcion, FuncionForm)
admin.site.register(Ventas, VentasForm)
admin.site.register(Ubicacion, UbicacionForm)
admin.site.register(Categoria, CategoriaAdmin)  # usa el admin con inline
