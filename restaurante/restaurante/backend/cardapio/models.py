# Importa models do pacote django.db
from django.db import models

#Cria uma classe que representa a tabela do cardapio
class Cardapio(models.Model):
    prato = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.CharField(max_length=200)

    #Retorna o prato
    def __str__(self):
        return self.prato   

# Create your models here.