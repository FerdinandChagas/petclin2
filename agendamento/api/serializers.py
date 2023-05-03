from rest_framework.serializers import ModelSerializer
from agendamento.models import Usuario

class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = [ 'nome', 'endereco', 'email', 'telefone', 'cpf', 'data_cadastro']