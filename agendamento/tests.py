from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from .models import Usuario
# Create your tests here.

class TestUsuarioViewSet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = Usuario(
            nome = "Dummy User",
            telefone = "234234234",
            email = "dummy@ufersa.edu.br",
            cpf = "41234241241234",
            endereco = "Rua Portugal, 287",
            data_cadastro = "2023-03-04",
        )
        self.user.save()
    
    def test_queryset(self):
        response = self.client.get('/api/usuarios/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'],1)