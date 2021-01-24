from rest_framework import routers
from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import current_user, UserList

Factura_list = views.FacturaViewSet.as_view({
    'get':'list',
    'post':'create'
})

Factura_detail = views.FacturaViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy',
})

detalleFactura_creation = views.FacturaViewSet.as_view({
    'post':'set_detalleFactura'
})

#Categoria crud
Categoria_list = views.CategoriaViewSet.as_view({
    'get':'list',
    'post':'create'
})

Categoria_detail = views.CategoriaViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy',
})

#Productos crud
Productos_list = views.ProductoViewSet.as_view({
    'get':'list',
    'post':'create'
})

Productos_detail = views.ProductoViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy',
})
urlpatterns = [
    path('factura/', Factura_list),
    path('factura/<int:pk>/', Factura_detail),
    path('factura/<int:pk>/detalleFactura/', detalleFactura_creation),
    path('categoria/',Categoria_list),
    path('categoria/<int:pk>/',Categoria_detail),
    path('producto/',Productos_list),
    path('producto/<int:pk>/',Productos_detail),
    path('usuario_actual/',current_user),
    path('usuarios/', UserList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
