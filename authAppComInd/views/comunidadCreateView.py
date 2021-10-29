from rest_framework                                     import status,views, generics
from rest_framework.response                            import Response
from rest_framework_simplejwt.serializers               import TokenObtainPairSerializer
from authAppComInd.serializers.comunidadSerializer      import ComunidadSerializer
from authAppComInd.models.comunidad                     import Comunidad
from rest_framework                                     import serializers

class ComunidadCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ComunidadSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
    
        return Response("comunidad creada", status=status.HTTP_201_CREATED)


class ComunidadListView(generics.ListAPIView):
    serializer_class = ComunidadSerializer
    def get_queryset(self):
        queryset = Comunidad.objects.all()
        return queryset

class ComunidadUpdateView(generics.UpdateAPIView):
    serializer_class   = ComunidadSerializer
    queryset           = Comunidad.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ComunidadDeleteView(generics.DestroyAPIView):
    serializer_class   = ComunidadSerializer
    queryset           = Comunidad.objects.all()

    def delete(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response("comunidad borrada", status=status.HTTP_204_NO_CONTENT)