from django.contrib import admin

from main.models import VMS, Brand, Gender, SKU

# Register your models here.
admin.site.register(Brand)
admin.site.register(Gender)
admin.site.register(SKU)
admin.site.register(VMS)