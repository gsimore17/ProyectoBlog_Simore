from django.urls import path
from pr_blogapp.views import ListaArticulosView, DetalleArticuloView, CrearArticuloView, EditarArticuloView,  BorrarArticuloView

#app_name = 'pr_blogapp' 

urlpatterns = [
    path('lista_articulos', ListaArticulosView.as_view(), name='lista_articulos'),
    path('article/<int:pk>', DetalleArticuloView.as_view(), name='detalle_articulo'),
    path('crear_articulo', CrearArticuloView.as_view(), name='crear_articulo'),
    path('editar_articulo/<int:pk>', EditarArticuloView.as_view(), name='editar_articulo'),
    path('borrar_articulo/<int:pk>', BorrarArticuloView.as_view(), name='borrar_articulo'),
]