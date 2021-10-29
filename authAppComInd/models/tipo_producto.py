from django.db   import models

producto_type = [
    ('tejido','tejido'),
    ('ceramica','ceramica'),
    ('joyeria','joyeria'),
    ('Orfebreria','Orfebreria'),
    ('tallado','tallado'),
]

class Tipo_producto(models.Model):
    id              = models.AutoField(primary_key=True)
    nombre_tipo_prod = models.CharField(max_length=12 ,choices = producto_type)

