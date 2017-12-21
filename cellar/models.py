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


class Barrel(models.Model):
    serial = models.CharField(max_length=8)

    SPIRITS = (
        ('b', 'Bourbon'),
        ('bm', 'Bourbon/Maple'),
        ('g', 'Gin'),
        ('r', 'Rum'),
        ('smw', 'Single Malt Whiskey'),
        ('t', 'Tequila'),
        ('w', 'Whiskey'),
    )

    spirit_profile = models.CharField(max_length=4, choices=SPIRITS, blank=True, default='bm')

    BARREL_STATUS = (
        ('a', 'Available'),
        ('i', 'In Use'),
    )

    status = models.CharField(max_length=1, choices=BARREL_STATUS, blank=True, default='a')

    def __str__(self):
        return self.serial
