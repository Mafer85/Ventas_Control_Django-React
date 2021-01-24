from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import viewsets, status, permissions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView

from todos.models import Vendedor, Categoria, Producto, Factura, detalleFactura
from .serializers import VendedorSerializer, CategoriaSerializer, ProductoSerializer, detalleFacturaSerializer, FacturaSerializer, UserSerializer, UserSerializerWithToken

@api_view(http_method_names=['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    permissions_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer=UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    @action(detail=True, methods=['post'])
    def set_detalleFactura(self, request, pk=None):

        my_factura = self.get_object()
        serializer = detalleFacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(factura=my_factura)
            return Response(serializer.data,
            status = status.HTTP_201_CREATED
            )

        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class =ProductoSerializer
