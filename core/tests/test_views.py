from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            "nome": "Felicity Jones",
            "email": "felicityjones@gmail.com",
            "assunto": "Meu assunto",
            "mensagem": "Minha mensagem"
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy("index"), data=self.dados)
        self.assertEquals(request.status_code, 302)  # Se caso esteja enviando os dados, retornará a requisição 302.
        # Que nada mais é o sucesso de requisições de envio de dados via POST http.

    def test_form_invalid(self):
        dados = {
            "nome": "Felicity Jones",
            "email": "felicityjones@gmail.com"
        }

        request = self.cliente.post(reverse_lazy("index"), data=dados)
        self.assertEquals(request.status_code, 200)  # Se caso não esteja enviando os dados, retornará a requisição 200.
        # Que nada mais é que o erro de envio de dados via POST http.


