from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from agendamento.models import Usuario
# Create your tests here.

class TestUsuarioViewSet(APITestCase):

    """ def setUp(self):
        self.client = APIClient()
    
    def test_create_user(self):
        data = {
            "nome" : "Dummy User",
            "telefone" : "234234234",
            "email" : "dummy@ufersa.edu.br",
            "cpf" : "41234241241234",
            "endereco" : "Rua Portugal, 287",
            "data_cadastro" : "2023-03-04",
        }
        response = self.client.post('/api/usuarios/', data=data)
        self.assertEqual(response.status_code, 201)
    
    def test_list_users(self):
        response = self.client.get('/api/usuarios/')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.data[0],1) """