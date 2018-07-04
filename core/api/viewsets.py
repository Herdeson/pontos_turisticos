from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return  PontoTuristico.objects.filter(aprovado=True)

    #def list(self, request,*args, **kwargs):
    #    return PontoTuristico.objects.all()
    # Listagem padrão

    def create(self, request,*args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    #def destroy(self, request, *args, **kwargs):
    #    pass

    #def retrieve(self, request,*args, **kwargs):
    #    pass

    #def update(self, request,*args, **kwargs):
    #    pass

    #Criar action personalizadas
    @action(methods=['get'], detail=True)
    def deununciar(self, request, pk=None):
        pass
