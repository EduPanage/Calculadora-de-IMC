from django.urls import path
from .views import calcular_imc, limpar_historico

urlpatterns = [
    path('', calcular_imc, name='calcular_imc'),
    path('limpar/', limpar_historico, name='limpar_historico'),
]