import datetime
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# class CustomModelViewSet(ModelViewSet):
#     # Define uma nova classe chamada `CustomModelViewSet` que herda de `ModelViewSet`.
#     # `ModelViewSet` é uma classe do Django REST framework que fornece ações padrão para criar, recuperar, atualizar e deletar instâncias de um modelo.

#     def create(self, request, *args, **kwargs):
#         # Define um método chamado `create` que lida com solicitações HTTP POST para criar uma nova instância de um modelo.
#         # `request` contém os dados da solicitação.
#         # `*args` e `**kwargs` permitem passar argumentos adicionais para o método.

#         serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
#         # Obtém um serializador adequado para o modelo associado, passando os dados da solicitação.
#         # `many=isinstance(request.data, list)` verifica se `request.data` é uma lista. Se for, `many` é definido como True, permitindo a criação de múltiplas instâncias de uma vez.

#         serializer.is_valid(raise_exception=True)
#         # Valida os dados do serializador. Se os dados não forem válidos, uma exceção será lançada.

#         self.perform_create(serializer)
#         # Chama o método `perform_create` para salvar a nova instância (ou instâncias) no banco de dados.

#         headers = self.get_success_headers(serializer.data)
#         # Obtém os cabeçalhos de sucesso que serão incluídos na resposta HTTP.
#         # Esses cabeçalhos geralmente contêm informações sobre a localização da nova instância criada.

#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#         # Retorna uma resposta HTTP com os dados do serializador (as novas instâncias criadas),
#         # um status HTTP 201 (Created), indicando que a criação foi bem-sucedida,
#         # e os cabeçalhos de sucesso.


class UsuarioCustomizadoView(ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = UsuarioCustomizado.objects.filter(id=user.id)        
        return queryset




class EmprestimoLivrosView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        user = request.user

    
        emprestimoAtivo = Emprestimo.objects.filter(usuarioFK=user, dataDevolucao__isnull=True).count()
        if emprestimoAtivo >= 3:
            return Response({'error': 'Você já possui 3 empréstimos corintiano ladrao'}, status=status.HTTP_400_BAD_REQUEST)

    
        livro_id = request.data.get('livro_id')
        try:
            livro = Livros.objects.get(id=livro_id, aprovado="A")
            
        except Livros.DoesNotExist:
            return Response({'error': 'Livro não disponível ou não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        if livro.quantidade > 0:
            
            # Crie o empréstimo (Emprestimo) se necessário
            emprestimo, created = Emprestimo.objects.get_or_create(usuarioFK=user, dataDevolucao__isnull=True, defaults={'devolucaoPrevista': (datetime.date.today() + datetime.timedelta(weeks=2))})

            # Crie o registro de EmprestimoLivros
            emprestimo_livro = EmprestimoLivros.objects.create(emprestimoFK=emprestimo, livroFK=livro, quantidade=1)
            livro.quantidade = livro.quantidade - 1
            livro.save()

            serializer = EmprestimoLivrosSerializer(emprestimo_livro)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status='deu erro viado')
    def get(self, request, *args, **kwargs):
        user = request.user

        emprestimos = Emprestimo.objects.filter(usuarioFK=user, dataDevolucao__isnull=True)


        serializer = EmprestimoSerializer(emprestimos, many=True)
        return Response(serializer.data)
    
    
class EmprestimoView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Emprestimo.objects.all() 
    serializer_class = EmprestimoSerializer
    
class LivrosView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Livros.objects.all() 
    serializer_class = LivrosSerializer

