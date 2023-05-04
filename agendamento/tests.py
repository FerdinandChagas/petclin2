from datetime import datetime as dt
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase

from .models import Usuario
# Create your tests here.

class TestUsuarioViewSet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = Usuario.objects.create(
            nome = 'Dummy User',
            telefone = '234234234',
            email = 'dummy@ufersa.edu.br',
            cpf = '41234241241234',
            endereco = 'Rua Portugal, 287',
            data_cadastro = dt.today(),
        )
        self.user.save()
    
    def test_queryset(self):
        response = self.client.get('api/usuarios/')
        self.assertEquals(response.status_code,404)
        #self.assertEqual(response.data['count'],0)