from django.contrib import admin
from .models import Categoria, Producto, Factura, detalleFactura,Vendedor

class VendedorAdmin(admin.ModelAdmin):
    pass

class CategoriaAdmin(admin.ModelAdmin):
    pass

class ProductoAdmin(admin.ModelAdmin):
    pass


class detalleFacturaInLine(admin.TabularInline):
    model = detalleFactura
    extra = 3

class FacturaAdmin(admin.ModelAdmin):
    inlines = [detalleFacturaInLine, ]
    
admin.site.register(Vendedor,VendedorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Factura, FacturaAdmin)
