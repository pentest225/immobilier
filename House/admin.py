from django.contrib import admin
from .models import House,HousePayementPeriod,HouseType

# Register your models here.

admin.site.register(House)
admin.site.register(HouseType)
admin.site.register(HousePayementPeriod)