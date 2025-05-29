from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from mainApp import views
from mainApp.views import EventosList, EventosDetail, VentasList

urlpatterns = [
    path("admin/", admin.site.urls),

    # Vistas HTML (frontend/backoffice)
    path('', views.index, name='index'), 
    path('comprar/<int:id>/', views.comprar, name='comprar'),
    path('ticket/<int:id>/', views.ticket, name='ticket'),

    # API REST
    path('api/eventos/', EventosList.as_view(), name='eventos-list'),
    path('api/eventos/<int:pk>/', EventosDetail.as_view(), name='eventos-detail'),
    path('api/ventas/', VentasList.as_view(), name='ventas-list'),

    # Categorías (vista dinámica según slug)
    path('categoria/<slug:categoria_slug>/', views.eventos_por_categoria, name='eventos_por_categoria'),
]

# Sirve archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
