from rest_framework import serializers
from .models import *


class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True






class LivrosSerializer(serializers.ModelSerializer):
    idade_display = serializers.SerializerMethodField()
    categoria_display = serializers.SerializerMethodField()
    formato_display = serializers.SerializerMethodField()
    aprovado_display = serializers.SerializerMethodField()

    def get_idade_display(self, obj):
        return dict(CLASSIFICACAO_INDICATIVA).get(obj.idade)

    def get_categoria_display(self, obj):
        return dict(CATEGORIA_LIVRO).get(obj.categoria)

    def get_formato_display(self, obj):
        return dict(FORMATO_LIVRO).get(obj.formato)

    def get_aprovado_display(self, obj):
        return dict(APROVACAO_LIVRO).get(obj.aprovado)

    class Meta:
        model = Livros
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emprestimo
        fields = '__all__'
        many = True


class EmprestimoLivrosSerializer(serializers.ModelSerializer):
    livroFK = LivrosSerializer

    class Meta:
        many = True
        model = EmprestimoLivros
        fields = '__all__'