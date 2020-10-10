from api import api
from flask import request, Response

from controllers import *

# @api.route('/api')
# def index():
#     return 'Hello World'

@api.route('/api/doc')
def index():
    response = validaCPF(request)
    return Response(f'{{"message": {response["message"]}}}', status=response["status"])