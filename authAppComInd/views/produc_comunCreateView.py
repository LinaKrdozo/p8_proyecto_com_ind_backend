from rest_framework                                     import status,views, generics
from rest_framework.response                            import Response
from rest_framework_simplejwt.serializers               import TokenObtainPairSerializer
from authAppComInd.serializers.produc_comunSerializer   import Produc_comunSerializer
from authAppComInd.models.produc_comun                  import Produc_comun
from rest_framework                                     import serializers

class Produc_comunCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = Produc_comunSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response("producto y comunidad creado", status=status.HTTP_201_CREATED)


class Produc_comunListView(generics.ListAPIView):
    serializer_class = Produc_comunSerializer
    def get_queryset(self):
        queryset = Produc_comun.objects.all()
        return queryset

