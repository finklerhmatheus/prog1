from django.contrib import admin

from .models import Produto, Cliente, Maquina

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor', 'funcao')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Maquina, MaquinaAdmin)