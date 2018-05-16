from django.contrib import admin

from .models import *

admin.site.register(Usuario)
admin.site.register(Sala)
admin.site.register(Insumo)
admin.site.register(Horario)
admin.site.register(Reserva)