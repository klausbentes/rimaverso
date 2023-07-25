from django.contrib import admin
from rimaverso.models import Dicionario

# Register your models here.

class ListandoPalavras(admin.ModelAdmin):
    list_display = ('palavra', 'pronuncia', 'rima')
    search_fields = ('palavra',)
    list_display_links = ('palavra', 'pronuncia', 'rima')
    list_filter = ('silabas',)
    ordering = ('id',)

admin.site.register(Dicionario, ListandoPalavras)