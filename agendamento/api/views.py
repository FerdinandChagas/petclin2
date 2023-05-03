from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from agendamento.api.serializers import UsuarioSerializer
from agendamento.models import Usuario

class UsuarioViewSet(ModelViewSet):

    serializer_class = UsuarioSerializer
    permissions_class = [ IsAuthenticated ]
    queryset = Usuario.objects.all()

