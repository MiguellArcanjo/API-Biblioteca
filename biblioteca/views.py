from rest_framework import viewsets
from biblioteca.models import Biblioteca, Livraria
from biblioteca.serializers import BibliotecaSerializers, LivrariaSerializers

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializers

class LivrariaViewSet(viewsets.ModelViewSet):
    queryset = Livraria.objects.all()
    serializer_class = LivrariaSerializers
