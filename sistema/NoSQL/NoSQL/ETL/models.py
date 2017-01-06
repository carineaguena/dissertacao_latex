# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ambiente(models.Model):
	tipo = models.CharField(max_length=200)

	def __str__(self):
		return self.tipo

class RepositorioDados(models.Model):
	ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
	conexao = models.CharField(max_length=200)
	dml = models.CharField(max_length=200)

