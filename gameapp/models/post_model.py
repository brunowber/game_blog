# -*- coding: utf-8 -*-
"""Model do Post"""

from __future__ import unicode_literals
from django.db import models
from gameapp.models.usuario_model import UsuarioModel


class PostModel(models.Model):
    """Classe para model de posts
    :param titulo: models.CharField(max_length=30)
    :param texto: models.CharField(max_length=300)
    :param curtidas: models.IntegerField(default=0)
    :param usuario: models.ForeignKey(UsuarioModel)"""

    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=300)
    curtidas = models.IntegerField(default=0)
    usuario = models.ForeignKey(UsuarioModel)

    class Meta:
        app_label = "gameapp"

    def __unicode__(self):
        return self.titulo

