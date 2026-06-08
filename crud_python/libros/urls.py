from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaLibros.as_view(), name='lista-libros'),
    path('<int:pk>', views.DetalleLibro.as_view(), name='detalle-libro'),
]