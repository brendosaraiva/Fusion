import uuid
from django.test import TestCase
from model_mommy import mommy  # busca a referência dos testes para checagem.

from core.models import get_file_path


class GetFilePathTestCase(TestCase):

    # Cria um arquivo png de teste, que servirá para medir tamanho da string.
    def setUp(self):  # método de configuração ou criação de atributos.
        self.filename = f"{uuid.uuid4()}.png"

    # Função de teste, sempre deve começar 'test_' na frente da função/método que
    # será usado para verificação.
    def test_get_file_path(self):
        arquivo = get_file_path(None, "teste.png")
        self.assertTrue(len(arquivo), len(self.filename))

# model_mommy cria valores automáticos para todos os campos dos models

# Criando testes utilizando TestCase com model_mommy


class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make("Servico")

    def test_st(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make("Cargo")

    def test_st(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = mommy.make("Funcionario")

    def test_st(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

# ou

# criando testes somente com model_mommy
"""
cargo = mommy.make("Cargo")
print(cargo)
funcionario = mommy.make("Funcionario")
print(funcionario)
servico = mommy.make("Servico")
print(servico)
feature = mommy.make("Feature")
print(feature)
cliente = mommy.make("Cliente")
print(cliente)
"""
# OBS: coverage só testa classes.
