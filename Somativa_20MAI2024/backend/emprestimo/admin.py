from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = UsuarioCustomizado
    list_display = ['id', 'email', 'cpf']
    list_display_links = ('id', 'email', 'cpf',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf', 'telefone', 'endereco',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions',)
        }),
    )
    search_fields = ['email',]
    ordering = ['email']
    

admin.site.register(UsuarioCustomizado, CustomUserAdmin)

# Adicione os related_names nos acessos reversos para evitar colisões
UsuarioCustomizado.groups.field.related_name = 'custom_user_groups'
UsuarioCustomizado.user_permissions.field.related_name = 'custom_user_permissions'
class AdminFoto(admin.ModelAdmin):
    list_display = ['id', 'url']
    list_display_links = ('id', 'url')
    search_fields = ('url',)
    list_per_page = 10
admin.site.register(Foto, AdminFoto)

class AdminLivros(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'editora', 'categoria', 'nota', 'valor', 'quantidade', 'idade', 'dataLancamento', 'publicacao', 'numeroPaginas', 'formato', 'codEdicao', 'aprovado']
    list_display_links = ('id', 'titulo', 'autor', 'editora')
    search_fields = ('titulo', 'autor__username', 'editora', 'categoria')
    list_filter = ('categoria', 'idade', 'formato', 'aprovado')
    date_hierarchy = 'dataLancamento'
    filter_horizontal = ('fotoFK',)
    list_per_page = 10

admin.site.register(Livros, AdminLivros)


class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['id', 'usuarioFK', 'dataEmprestimo', 'devolucaoPrevista', 'dataDevolucao', 'status']
    list_display_links = ('id', 'usuarioFK', 'dataEmprestimo', 'devolucaoPrevista')
    search_fields = ('usuarioFK__username',)
    list_filter = ('status', 'dataEmprestimo', 'devolucaoPrevista')
    list_per_page = 10

admin.site.register(Emprestimo, AdminEmprestimo)

class AdminEmprestimoLivros(admin.ModelAdmin):
    list_display = ['id', 'livroFK', 'emprestimoFK', 'quantidade']
    list_display_links = ('id', 'livroFK', 'emprestimoFK')
    search_fields = ('livroFK__titulo', 'emprestimoFK__usuarioFK__username')
    list_filter = ('livroFK', 'emprestimoFK')
    list_per_page = 10

admin.site.register(EmprestimoLivros, AdminEmprestimoLivros)