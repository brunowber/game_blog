# coding: utf-8
"""Model de usuários"""

from django.db import models
from django.contrib.auth.models import User
from gameapp.models.post_model import PostModel
from gameapp.models.comentario_model import ComentarioModel
from gameapp.models.curtir_model import CurtirModel


class UsuarioModel(User):
    post = models.ForeignKey(PostModel)
    comentario = models.ManyToManyField(ComentarioModel)
    curtir = models.ManyToManyField(CurtirModel)

