from django.contrib import admin
from empleado.models import Empleado, Puesto, UserProfileInfo
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Puesto)
admin.site.register(UserProfileInfo)
