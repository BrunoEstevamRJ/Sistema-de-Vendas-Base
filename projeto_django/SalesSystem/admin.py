from django.contrib import admin
from SalesSystem.models import Clientes
from django.contrib.admin.options import ModelAdmin, TabularInline


class ClientesAdmin(admin.ModelAdmin):
    list_display = (
        'NomeRazao',
        'Contato',
        'Telefone', 
        'Celular',
        'CpfCnpj',
        'Estado'
        )
    
    search_fields = (
        'NomeRazao',
        )
    
    ordering = (
        'NomeRazao',
        )

admin.site.register(Clientes,ClientesAdmin)