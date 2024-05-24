from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()

router.register(r'livros',LivrosView)
router.register(r'emprestimos',EmprestimoView)
router.register(r'emprestimos-livros',EmprestimoLivrosView, basename='emprestimos-livros')
router.register(r'usuarios',UsuarioCustomizadoView)

urlpatterns = router.urls