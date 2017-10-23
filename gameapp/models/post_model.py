# coding: utf-8
"""Model do Post"""

from django.db import models
from gameapp.models.usuario_model import UsuarioModel


class PostModel(models):
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=200)
    cutir = models.BooleanField(default=False)
    usuario = models.ForeignKey(UsuarioModel)

