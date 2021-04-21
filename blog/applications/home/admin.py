from django.contrib import admin
from .models import (
    Home,
    Suscriber,
    Contacto,
)
# Register your models here.
admin.site.register(Home)
admin.site.register(Suscriber)
admin.site.register(Contacto)