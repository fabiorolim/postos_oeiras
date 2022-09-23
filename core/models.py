from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posto(models.Model):
    nome_fantasia = models.CharField('nome', max_length=100)
    localizacao = models.URLField('localizacao', blank=True)
    slug = models.SlugField('slug', blank=True, max_length=50)
    foto = models.URLField('foto', blank=True)
    site = models.URLField('site', blank=True)
    telefone = models.CharField('telefone', max_length=11, blank=True)
    email = models.EmailField('email', blank=True)
    adm = models.ForeignKey(User, on_delete=models.CASCADE)
    data_add = models.DateField('data', auto_now_add=True)
    ativo = models.BooleanField('ativo', default=True)

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        verbose_name = 'Posto'
        verbose_name_plural = 'Postos'


class Combustivel(models.Model):
    nome = models.CharField('nome', max_length=30)
    slug = models.SlugField('slug', blank=True, max_length=50)
    data_add = models.DateField('data', auto_now_add=True)
    ativo = models.BooleanField('ativo', default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustíveis'


class Preco(models.Model):
    combustivel = models.ForeignKey(Combustivel, on_delete=models.CASCADE, related_query_name='combustivel')
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, related_name='posto')
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    adm = models.ForeignKey(User, on_delete=models.CASCADE)
    data_add = models.DateField('data', auto_now_add=True)

    def __str__(self):
        return str(self.preco)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'
