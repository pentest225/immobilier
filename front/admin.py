from ast import Constant
from django.contrib import admin
from .models import SiteInfo,Slider,Contact
# Register your models here.

admin.site.register(SiteInfo)
admin.site.register(Slider)
admin.site.register(Contact)