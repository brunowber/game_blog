# coding: utf-8
"""Model de comentários"""

from django.db import models
from django.utils.datetime_safe import datetime

from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.post_model import PostModel


class ComentarioModel(models.Model):
    """model de comentários"""

    comentario = models.CharField(max_length=1000)
    like = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    usuario = models.ForeignKey(UsuarioModel)
    post = models.ForeignKey(PostModel)

    class Meta:
        app_label = "gameapp"

    def __unicode__(self):
        return self.post.titulo
