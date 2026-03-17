from django.contrib import admin
from .models import Projeto, Contato

admin.site.site_header = "Matheus Junior | Backend Management"
admin.site.index_title = "Painel de Controle de Dados"

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tecnologias', 'link_github')
    search_fields = ('titulo', 'tecnologias')
    list_filter = ('tecnologias',)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio')
    ordering = ('-data_envio',)
    search_fields = ('nome', 'email')
    list_filter = ('data_envio',)
    readonly_fields = ('nome', 'email', 'mensagem', 'data_envio')