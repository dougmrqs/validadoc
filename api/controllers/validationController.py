from services.valida_CPF import CPF

def validaCPF(req):
    if req.args.get('cpf'):
        cpf = CPF(req.args.get('cpf'))
        if cpf.check():
            return {"message": "CPF Válido", "status": 200}
        else:
            return {"message": "CPF Inválido", "status": 400}