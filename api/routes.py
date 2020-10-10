from api import api
from flask import request, Response

from controllers import *

@api.route('/')
def index():
    return '<h1>Instruções:</h1> \
            <span>GET /api/doc?cpf=55829512025 \
            <br><br> \
            <span>Deve retornar 200 se o CPF for válido ou 400 se for inválido.'

@api.route('/api/doc')
def validadoc():
    response = validaCPF(request)
    return Response(f'{{"message": {response["message"]}}}', status=response["status"])