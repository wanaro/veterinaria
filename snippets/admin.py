from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Cliente)
admin.site.register(Veterinario)
admin.site.register(Consulta)
admin.site.register(Diagnostico)