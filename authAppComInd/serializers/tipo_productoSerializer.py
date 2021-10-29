from authAppComInd.models.tipo_producto import Tipo_producto
from rest_framework                     import serializers

class Tipo_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Tipo_producto
        fields = ['nombre_tipo_prod']
    
    def to_representation(self, obj):
        tipo_producto   = Tipo_producto.objects.get(id=obj.id)
        return {
            'id'               : tipo_producto.id,
            'nombre_tipo_prod' : tipo_prod.nombre_tipo_prod
        }