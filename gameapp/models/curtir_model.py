# -*- coding: utf-8 -*-
"""Model de curtidas"""

from __future__ import unicode_literals
from django.db import models
from gameapp.models.comentario_model import ComentarioModel
from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.post_model import PostModel


class CurtirModel(models.Model):
    """Classa da model de curtidas
    :param coment: models.ForeignKey(ComentarioModel, default=False)
    :param usuario: models.ForeignKey(UsuarioModel)
    :param post: models.ForeignKey(PostModel, default=False)
    """

    coment = models.ForeignKey(ComentarioModel, default=False)
    usuario = models.ForeignKey(UsuarioModel)
    post = models.ForeignKey(PostModel, default=False)

    class Meta:
        app_label = "gameapp"

    def __unicode__(self):
        return self.usuario.username
