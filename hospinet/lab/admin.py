from django.contrib import admin

from .models import Resultado

@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
	pass