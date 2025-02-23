from django.contrib import admin
from .models import *


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'station', 'notification', 'date', 'client_name', 'place_of_transfer', 'locomotive',
                    'route_belonging', 'client_representative')
    list_filter = ('number', 'date', 'station')
    list_display_links = ['id', 'number', 'station', 'notification', 'date', 'client_name', 'place_of_transfer',
                          'locomotive', 'route_belonging', 'client_representative', ]


# Register your models here.

class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'document', 'wagon', 'container_and_size', 'type', 'control_mark', 'operation', 'cargo_names', 'note')
    list_filter = ('document', 'wagon', 'container_and_size')
    list_display_links = ['document', 'wagon', 'container_and_size', 'type', 'control_mark', 'operation', 'cargo_names',
                          'note',
                          ]


admin.site.register(Document, DocumentAdmin)
admin.site.register(Cargo, CargoAdmin)
