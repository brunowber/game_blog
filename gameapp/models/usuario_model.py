# coding: utf-8
"""Model de usuários"""

from django.db import models
from django.contrib.auth.models import User
# from curtir_model import CurtirModel


class UsuarioModel(User):
    jogo = models.CharField(max_length=20, default=None)
    # curtidas = models.ManyToManyField(CurtirModel)

    class Meta:
        app_label = "gameapp"
