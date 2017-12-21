from django.db import models
from django.utils import timezone

# Create your models here.

class Tank(models.Model):
    title = models.CharField(max_length=4)

    TANK_VOLUMES = (
        ('20', '20 BBL'),
        ('20.96', '20.96 BBL'),
        ('25.8', '25.8 BBL'),
        ('40', '40 BBL'),
    )
    volume = models.DecimalField(choices=TANK_VOLUMES, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
