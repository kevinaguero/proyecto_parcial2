from django.contrib import admin

from apps.vianda.models import InfoSolicitudVianda, ItemVianda

# Register your models here.

admin.site.register(InfoSolicitudVianda)
admin.site.register(ItemVianda)