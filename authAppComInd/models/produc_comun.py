from django.db   import models
from .comunidad  import Comunidad
from .producto   import Producto

class Produc_comun(models.Model):
    id         = models.AutoField(primary_key=True)
    comunidad  = models.ForeignKey(Comunidad, related_name='produc_comun', on_delete = models.CASCADE)
    producto   = models.ForeignKey(Producto, related_name='produc_comun', on_delete = models.CASCADE)
