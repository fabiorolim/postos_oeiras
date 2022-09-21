from django.contrib import admin
from .models import Posto, Preco, Combustivel

admin.site.register(Preco)
admin.site.register(Posto)
admin.site.register(Combustivel)
