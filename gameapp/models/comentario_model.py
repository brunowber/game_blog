# -*- coding: utf-8 -*-
"""Model de comentários"""

from __future__ import unicode_literals
from django.db import models
from django.utils.datetime_safe import datetime

from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.post_model import PostModel


class ComentarioModel(models.Model):
    """
    Classe para model de Comentários

    :param comentario: models.CharField(max_length=1000)
    :param like: models.IntegerField()
    :param date: models.DateTimeField(default=datetime.now, blank=True)
    :param usuario: models.ForeignKey(UsuarioModel)
    :param post: models.ForeignKey(PostModel)
    """

    comentario = models.CharField(max_length=1000)
    like = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    usuario = models.ForeignKey(UsuarioModel)
    post = models.ForeignKey(PostModel)

    class Meta:
        app_label = "gameapp"

    def __unicode__(self):
        return self.post.titulo
