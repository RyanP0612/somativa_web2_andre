from rest_framework import serializers
from .models import *


class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True





class LivrosSerializer(serializers.ModelSerializer):

 
    class Meta:
        model = Livros
        fields = '__all__'
        many = True


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