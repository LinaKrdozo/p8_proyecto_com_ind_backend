from authAppComInd.models.produc_comun                import Produc_comun
from rest_framework                                   import serializers
from authAppComInd.models.producto                    import Producto
from authAppComInd.serializers.productoSerializer     import ProductoSerializer
from authAppComInd.models.comunidad                   import Comunidad
from authAppComInd.serializers.comunidadSerializer    import ComunidadSerializer


class Produc_comunSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Produc_comun
        fields = ['comunidad', 'producto']
    
    def create(self, validated_data):
        produc_comunInstance  = Produc_comun.objects.create(**validated_data)
        return produc_comunInstance


    def to_representation(self,obj):
        comunidad    = Comunidad.objects.get(produc_comun=obj.id)
        producto     = Producto.objects.get(produc_comun=obj.id)
        produc_comun = Produc_comun.objects.get(id=obj.id)
        return{
            'id'         : produc_comun.id,
            'comunidad'  : {
                'id'              : comunidad.id,
                'nombreComunidad' : comunidad.nombreComunidad
            },
            'producto'   : {
                 'id'             : producto.id,
                 'nombreProducto' : producto.nombreProducto,
                 'caracteristica' : producto.caracteristica,
                 'cantidad'       : producto.cantidad    
            }
        }