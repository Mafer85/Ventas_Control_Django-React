from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from todos.models import Vendedor, Categoria, Producto, Factura, detalleFactura

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        
class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    class Meta:
        model = User
        fields = ('token','username','password')

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields= ('user','c')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class detalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = detalleFactura
        fields = ('__all__')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','precio','descripcion','existencias','categoria','vendedor')


class FacturaSerializer(serializers.ModelSerializer):
    numfactura = detalleFacturaSerializer(many=True, allow_null=True)
    class Meta:
        model = Factura
        fields = ('id','nombre_cliente','nit_cliente','fecha','numfactura','total')
