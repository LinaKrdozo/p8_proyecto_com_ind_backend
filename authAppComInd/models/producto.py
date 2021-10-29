from django.db   import models
from .tipo_producto     import Tipo_producto

class Producto(models.Model):
    id              = models.AutoField(primary_key=True)
    nombreProducto  = models.CharField(max_length=50)
    caracteristica  = models.CharField(max_length=100)
    cantidad        = models.IntegerField(default = 0)
    tipo_producto   = models.ForeignKey(Tipo_producto, related_name='producto', on_delete = models.CASCADE)

    def save(self, **kwargs):
        super().save(**kwargs)