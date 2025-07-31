from django.shortcuts import render, redirect
from .models import IMC

def calcular_imc(request):
    resultado = None

    historico_ids = request.session.get('historico_ids', [])
    historico = IMC.objects.filter(id__in=historico_ids).order_by('-data')

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
            peso=peso,
            altura=altura,
            imc=imc,
            classificacao=classificacao
        )
        novo_imc.save()

        historico_ids.append(novo_imc.id)
        request.session['historico_ids'] = historico_ids

        request.session['resultado'] = {
            'imc': round(imc, 2),
            'classificacao': classificacao
        }

        return redirect('calcular_imc')

    resultado = request.session.pop('resultado', None)

    return render(request, 'calculadora/index.html', {
        'resultado': resultado,
        'historico': historico
    })


def limpar_historico(request):
    if 'historico_ids' in request.session:
        del request.session['historico_ids']
    if 'resultado' in request.session:
        del request.session['resultado']
    return redirect('calcular_imc')
