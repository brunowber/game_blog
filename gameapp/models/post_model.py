# coding: utf-8
"""Model do Post"""

from django.db import models
from usuario_model import UsuarioModel


class PostModel(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=300)
    curtidas = models.IntegerField(default=0)
    usuario = models.ForeignKey(UsuarioModel)

    class Meta:
        app_label = "gameapp"

    def __unicode__(self):
        return self.titulo

