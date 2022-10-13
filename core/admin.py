from django.contrib import admin
from .models import Posto, Preco, Combustivel


class PostoAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'slug', 'adm', 'ativo',)
    prepopulated_fields = {'slug': ('nome_fantasia',)}
    readonly_fields = ('adm',)
    list_filter = ('ativo',)

    def save_model(self, request, obj, form, change):
        obj.adm = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)

        return Posto.objects.filter(adm=request.user).filter(ativo=True)


class CombustivelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'ativo')
    prepopulated_fields = {'slug': ('nome',)}
    list_filter = ('ativo',)


class PrecoAdmin(admin.ModelAdmin):
    list_display = ('preco', 'combustivel', 'posto', 'adm', 'data_add')
    readonly_fields = 'adm',
    list_filter = 'combustivel',

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)

        return Preco.objects.filter(adm=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'posto':
            kwargs["queryset"] = Posto.objects.filter(adm=request.user).filter(ativo=True)

        if db_field.name == 'combustivel':
            kwargs["queryset"] = Combustivel.objects.filter(ativo=True)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.adm = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Preco, PrecoAdmin)
admin.site.register(Posto, PostoAdmin)
admin.site.register(Combustivel, CombustivelAdmin)
