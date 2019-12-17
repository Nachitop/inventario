from django.contrib import admin
from facultades.models import Edificio, Ubicacion
# Register your models here.
# admin.site.register(Edificio)
# admin.site.register(Ubicacion)
@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):

    list_display = ('pk', 'nombre', 'created', 'modified')
    list_display_links = ('pk', 'nombre')
    list_filter = (
        'created',
        'modified',
    )

    search_fields = ('nombre',)
    fieldsets = (
        (None, {
            'fields': (
                ('nombre',),
                ('status',)
            ),
        }),
    )


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):

    list_display = ('pk', 'nombre', 'edificio', 'created', 'modified')
    list_display_links = ('pk', 'nombre')
    list_filter = (
        'edificio__nombre',
        'created',
        'modified',
    )

    search_fields = ('nombre',)

    fieldsets = (
        (None, {
            'fields': (
                ('nombre',),
                ('edificio',),
                ('status',)
            ),
        }),
    )
