from rest_framework import serializers
from biblioteca.models import Biblioteca, Livraria

class BibliotecaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '__all__'

class LivrariaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livraria
        fields = '__all__'