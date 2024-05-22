from rest_framework import serializers
from .models import *


class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True



class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Foto
        fields = '__all__'
        many = True

class LivrosSerializer(serializers.ModelSerializer):
    #fotos = FotoSerializer(read_only=True) #fazer o join com tabelas separadas
    fotoFK = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    ) #join com many to many field
 
    class Meta:
        model = Livros
        fields = '__all__'
        many = True


class EmprestimoSerializer(serializers.ModelSerializer):
    #usuarioFK = UsuarioCustomizadoSerializer(read_only=True)
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