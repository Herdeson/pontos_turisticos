from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializer import AtracaoSerializer

class AtracaoViewset(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
