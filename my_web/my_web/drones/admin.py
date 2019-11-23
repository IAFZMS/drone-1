from django.contrib import admin

from .models import (
	Dron,
	camara)
 
class dronAdmin(admin.ModelAdmin):
	pass
admin.site.register(Dron,dronAdmin) 
class camaraAdmin(admin.ModelAdmin):
	pass
admin.site.register(camara,camaraAdmin)


 