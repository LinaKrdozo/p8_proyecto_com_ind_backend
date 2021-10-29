from django.contrib import admin

from .models.region import Region
from .models.comunidad import Comunidad
from .models.produc_comun import Produc_comun
from .models.producto import Producto
from .models.tipo_producto import Tipo_producto

admin.site.register(Region)
admin.site.register(Comunidad)
admin.site.register(Produc_comun)
admin.site.register(Producto)
admin.site.register(Tipo_producto)

