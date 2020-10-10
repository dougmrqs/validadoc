import pytest

from api.services.valida_CPF import CPF

num1 = '32948239413'
num2 = '22222222222'
num3 = '08540705087'
num4 = '08540705086'


### Test Valida CPF

# should return False
def test_cpf1():
    cpf1 = CPF(num1)
    cpf2 = CPF(num2)
    cpf3 = CPF(num3)
    cpf4 = CPF(num4)
    assert cpf1.check() == False
    assert cpf2.check() == False
    assert cpf3.check() == True
    assert cpf4.check() == False