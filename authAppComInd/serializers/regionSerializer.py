from authAppComInd.models.region                   import Region
from rest_framework                                import serializers

class RegionSerializer(serializers.ModelSerializer):
    #comunidad = ComunidadSerializer()
    class Meta:
        model  = Region
        fields = ['nombreRegion']

    def to_representation(self, obj):
        region    = Region.objects.get(id=obj.id)
       # comunidad = Comunidad.objects.get(id=obj.comunidad)
        return {
            'id'           : region.id,
            'nombreRegion' : region.nombreRegion
        }
        