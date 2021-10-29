from django.db import models

region_type = [
    ('Caribe', 'Caribe'),
    ('Andina', 'Andina'),
    ('Pacifico', 'Pacifico'),
    ('Orinoquia', 'Orinoquia'),
    ('Amazonia', 'Amazonia'),
    ('Insular', 'Insular'),
]

class Region(models.Model):
    id           = models.AutoField(primary_key=True)
    nombreRegion = models.CharField(max_length=12, choices = region_type)
