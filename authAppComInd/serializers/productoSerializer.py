from authAppComInd.models.producto                      import Producto
from authAppComInd.models.tipo_producto                 import Tipo_producto
from authAppComInd.serializers.tipo_productoSerializer  import Tipo_productoSerializer
from rest_framework                                     import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Producto
        fields = ['nombreProducto', 'caracteristica', 'cantidad', 'tipo_producto']
    
    def create(self, validated_data):
        #tipo_productoData = validated_data.pop('tipo_producto')
        productoInstance  = Producto.objects.create(**validated_data)
        #Tipo_producto.objects.create(producto = productoInstance, **tipo_productoData)
        
        return productoInstance
    
    def to_representation(self, obj):
        producto       = Producto.objects.get(id=obj.id)
        tipo_producto  = Tipo_producto.objects.get(producto=obj.id)
        return {
            'id'             : producto.id,
            'nombreProducto' : producto.nombreProducto,
            'caracteristica' : producto.caracteristica,
            'cantidad'       : producto.cantidad,
            'tipo_producto'  : {
                  'id'              : tipo_producto.id,
                  'nombre_tipo_prod': tipo_producto.nombre_tipo_prod
            }
        }

