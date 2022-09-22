from django.contrib import admin
from .models import Posto, Preco, Combustivel


class PostoAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'slug', 'administrador', 'ativo',)


class CombustivelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'ativo')


class PrecoAdmin(admin.ModelAdmin):
    list_display = ('preco', 'posto', 'administrador', 'data_add')


admin.site.register(Preco, PrecoAdmin)
admin.site.register(Posto, PostoAdmin)
admin.site.register(Combustivel, CombustivelAdmin)
