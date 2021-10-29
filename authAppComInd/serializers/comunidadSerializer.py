from authAppComInd.models.comunidad              import Comunidad
from authAppComInd.models.region                 import Region
from authAppComInd.serializers.regionSerializer  import RegionSerializer
from rest_framework                              import serializers
 

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comunidad
        fields = ['nombreComunidad','region']

    def create(self, validated_data):
        #regionData = validated_data.pop('region')
        comunidadInstance = Comunidad.objects.create(**validated_data)
        #Region.objects.create(comunidad = comunidadInstance, **regionData)
        return comunidadInstance

    def to_representation(self,obj):
        comunidad = Comunidad.objects.get(id=obj.id)
        region    = Region.objects.get(comunidad=obj.id)
        return{
            'id'              : comunidad.id,
            'nombreComunidad' : comunidad.nombreComunidad,
            'region'  : {
                'id'           : region.id,
                'nombreRegion' : region.nombreRegion
            }
        }

    
    