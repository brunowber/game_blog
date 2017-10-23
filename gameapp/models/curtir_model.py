# coding: utf-8
"""Model de curtidas"""

from django.db import models
from gameapp.models.usuario_model import UsuarioModel


class CurtirModel(models):
    comentario = models.CharField(max_length=200)
    like = models.IntegerField()

    usuario = models.ForeignKey(UsuarioModel)
