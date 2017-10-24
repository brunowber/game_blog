# coding: utf-8
"""Model de curtidas"""

from django.db import models
from gameapp.models import UsuarioModel
from gameapp.models import ComentarioModel


class CurtirModel(models.Model):

    usuario = models.ForeignKey(UsuarioModel)
    comententario = models.ForeignKey(ComentarioModel)

    class Meta:
        app_label = "gameapp"