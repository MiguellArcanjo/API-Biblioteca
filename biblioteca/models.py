from django.db import models

# Create your models here.

class Livraria(models.Model):
    nomeLivraria = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'Você vai vender o livro na livraria: {self.nomeLivraria}'


class Biblioteca(models.Model):
    tituloLivro = models.CharField(max_length=100)
    autorLivro = models.CharField(max_length=100)
    preco = models.FloatField()
    livraria = models.ForeignKey(
        Livraria,
        max_length=100,
        on_delete=models.CASCADE
    )






