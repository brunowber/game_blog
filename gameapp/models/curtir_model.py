# -*- coding: utf-8 -*-
"""Model de curtidas"""

from django.db import models
from gameapp.models.comentario_model import ComentarioModel
from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.post_model import PostModel


class CurtirModel(models.Model):

    coment = models.ForeignKey(ComentarioModel, default=False)
    usuario = models.ForeignKey(UsuarioModel)
    post = models.ForeignKey(PostModel, default=False)

    class Meta:
        app_label = "gameapp"
