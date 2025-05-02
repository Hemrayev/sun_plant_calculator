from django.contrib.auth.models import User
from django.db import models
from .choices import *


# class CalculatedPanels(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     panel_name = models.CharField(max_length=255)
#     square_meters = models.FloatField()
#     count_of_panels = models.IntegerField()
#     degree = models.FloatField()
#     inventor_type = models.PositiveSmallIntegerField(choices=TYPE_OF_INVENTOR,default=1)
#     inventor_count = models.IntegerField()
#     type_of_akb = models.PositiveSmallIntegerField(choices=TYPE_OF_AKB,default=1)
#     akb_power = models.IntegerField()

class SolarPanels(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ady')
    power = models.FloatField(default=100.0, verbose_name='Kuwwaty')
    price = models.FloatField(default=0.0, verbose_name='Bahasy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gün paneli'
        verbose_name_plural = 'Gün panelleri'


class InvertersModel(models.Model):
    INVERTER_TYPES = (
        ('TOR', 'Tor Inverter'),
        ('GIBRID', 'Gibrid Inverter'),
    )
    type = models.CharField(max_length=10, choices=INVERTER_TYPES, help_text="Type of inverter")
    name = models.CharField(max_length=255, verbose_name='Ady')
    power = models.FloatField(default=100.0, verbose_name='Kuwwaty')
    price = models.FloatField(default=0.0, verbose_name='Bahasy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Inwentor'
        verbose_name_plural = 'Inwentorlar'


class BatteryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ady')
    price = models.FloatField(default=0.0, verbose_name='Bahasy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Batareýa'
        verbose_name_plural = 'Batareýalar'
