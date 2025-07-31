from django.shortcuts import render
from .models import IMC

def calcular_imc(request):

    resultado = None

    historico = IMC.objects.order_by('-data')[:5]

    if request.method == 'POST':    
            peso = float(request.POST['peso'])
            altura = float(request.POST['altura'])
        
            imc = peso / (altura * altura)

            if imc < 16:
             classificacao = "Magreza Grave"
            elif imc < 17:
              classificacao = "Magreza Moderada"
            elif imc < 18.5:
             classificacao = "Magreza Leve"
            elif imc < 25:
             classificacao = "Saudável"
            elif imc < 30:
                classificacao = "Sobrepeso"
            elif imc < 35:
                classificacao = "Obesidade Grau I"
            elif imc < 40:
                classificacao = "Obesidade Grau II"
            else:
                classificacao = "Obesidade Grau III"

            novo_imc = IMC(
               peso = peso,
               altura = altura,
               imc = imc,
               classificacao = classificacao
            )

            novo_imc.save()

            resultado = {
                'imc': round(imc, 2),
                'classificacao': classificacao
            }
    
    return render(request, 'calculadora/index.html', {
        'resultado': resultado,
        'historico': historico
       })