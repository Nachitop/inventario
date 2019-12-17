from django.contrib import admin
from equipos.models import Marca, TipoEquipo, Equipo
# Register your models here.

#admin.site.register(Marca)
#admin.site.register(TipoEquipo)
#admin.site.register(Equipo)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):

    list_display = ('pk','nombre','created','modified')
    list_display_links = ('pk','nombre')
    list_filter=(
        'created',
        'modified',
    )

    search_fields = ('nombre',)

@admin.register(TipoEquipo)
class TipoEquipoAdmin(admin.ModelAdmin):

    list_display = ('pk','nombre','created','modified')
    list_display_links = ('pk','nombre')
    list_filter=(
        'created',
        'modified',
    )

    search_fields = ('nombre',)

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):

    list_display = ('pk','codigo','descripcion','marca','tipo_equipo','status','created','modified')
    list_display_links = ('pk','codigo')
    list_filter=(
        
        'marca__nombre',
        'tipo_equipo__nombre',
        'status',
        'created',
        'modified',
    )

    search_fields = ('codigo',)