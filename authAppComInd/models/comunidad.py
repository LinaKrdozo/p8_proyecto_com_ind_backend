from django.db   import models
from .region     import Region

class Comunidad(models.Model):
    id              = models.AutoField(primary_key=True)
    nombreComunidad = models.CharField(max_length=50)
    region          = models.ForeignKey(Region, related_name='comunidad', on_delete = models.CASCADE  )

    def save(self, **kwargs):
        super().save(**kwargs)