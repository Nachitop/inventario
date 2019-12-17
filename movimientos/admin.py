from django.contrib import admin
from movimientos.models import Movimiento
# Register your models here.
#admin.site.register(Movimiento)

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):

    list_display = ('pk','numero_cuenta','equipo','ubicacion','status','created','modified')
    list_display_links = ('pk','numero_cuenta','equipo')
    list_filter=(
        'ubicacion__nombre',
 
        'status',
        'created',
        'modified',
    )

    search_fields = ('numero_cuenta','equipo__marca__nombre','equipo__tipo_equipo__nombre',)