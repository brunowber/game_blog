# coding: utf-8
"""Model de comentários"""

from django.db import models
from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.post_model import PostModel


class ComentarioModel(models.Model):
    """model de comentários"""

    comentario = models.CharField(max_length=300)
    like = models.IntegerField()

    usuario = models.ForeignKey(UsuarioModel)
    post = models.ForeignKey(PostModel)

    class Meta:
        app_label = "gameapp"
