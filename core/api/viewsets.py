from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated, IsAdminUser, )
    filter_backends = (SearchFilter,)
    search_fields =('nome', 'descricao', 'endereco__linha1', )

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()
        if id:
            #queryset = PontoTuristico.objects.filter(pk=id)
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)
        return queryset
        #return  PontoTuristico.objects.filter(aprovado=True)

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
