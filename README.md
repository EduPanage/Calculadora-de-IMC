# Calculadora de IMC com Django

Projeto simples de uma calculadora de IMC (Índice de Massa Corporal) usando Django, HTML e CSS.

## Funcionalidades

- Entrada de peso e altura para calcular o IMC.
- Exibição do resultado com classificação.
- Histórico dos últimos cálculos salvos no banco de dados.
- Layout responsivo e estilizado com CSS.

## Requisitos

- Python 3.8+
- Django 4.x
- Virtualenv (opcional, mas recomendado)

## Instalação

1. Clone o repositório:

git clone https://github.com/EduPanage/Calculadora-de-IMC.git
cd Calculadora-de-IMC

2. Crie o ambiente virtual:

  python -m venv venv
  venv/Scripts/activate

3. Instale as dependencias:

  pip install -r requirements.txt

4. Aplique as migrações:

   python manage.py migrate

5. Rode o servidor:

   python manage.py runserver

6. Coloque no seu navegador:

   http://127.0.0.1:8000/
