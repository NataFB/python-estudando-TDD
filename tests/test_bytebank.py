from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_11_01_2000_deve_retornar_23(self):
        # given-contexto
        entrada = '11/01/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1000)

        # when-ação
        resultado = funcionario_teste.idade()

        # Then-desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Natanael_Barbosa_deve_retornar_Barbosa(self):
        # given-contexto
        entrada = 'Natanael Barbosa '
        esperado = 'Barbosa'

        natanael = Funcionario(entrada, '11/01/2000', 1000)

        # when-ação
        resultado = natanael.sobrenome()

        # Then-desfecho
        assert resultado == esperado

    def test_quando_drecescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome,'11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 10000000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

