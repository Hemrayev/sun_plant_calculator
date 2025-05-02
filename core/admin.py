from django.contrib import admin
from .models import SolarPanels, InvertersModel, BatteryModel

admin.site.register(SolarPanels)
admin.site.register(InvertersModel)
admin.site.register(BatteryModel)
