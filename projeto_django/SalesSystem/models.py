# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Clientes(models.Model):
    NomeRazao = models.CharField('Nome/Razão social',max_length=50,unique=False,blank=False)
    CpfCnpj = models.CharField('CPF/CNPJ',max_length=50,blank=True)
    InscEstadual = models.CharField('Inscrição estadual', max_length=50, blank=True)
    Telefone = models.CharField('Telefone',max_length=50,blank=True)
    Celular = models.CharField('Celular',max_length=50,blank=True)
    Contato = models.CharField('Contato',max_length=50,unique=False,blank=True)
    Email = models.EmailField('E-mail', blank = False,unique = False)
    Status = models.CharField('Státus', max_length=10,default='ATIVO', blank=False, choices=(
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO'),
        ('EXCLUIDO', 'EXCLUIDO')
    ))
    Cep = models.CharField('CEP', max_length=10, unique=False, blank=True)
    Endereco = models.CharField('Endereço', max_length=100, unique=False, blank=True)
    Bairro = models.CharField('Bairro', max_length=50, unique=False, blank=True)
    Cidade = models.CharField('Cidade', max_length=50, unique=False, blank=False)
    Estado = models.CharField('Estado', max_length=2, blank=False)
    Observacoes = models.TextField('Observações', max_length=200, blank=True)
    Usuario = models.ForeignKey(User,null=True,  on_delete=models.CASCADE)    
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.NomeRazao
    class Meta:
        ordering = ('NomeRazao',)
