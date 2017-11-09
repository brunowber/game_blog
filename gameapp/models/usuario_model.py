# -*- coding: utf-8 -*-
"""Model de usuários"""

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UsuarioModel(User):
    """Classe para model de usuários
    :param jogo: models.CharmField(max_lenght=20, default=None)"""

    jogo = models.CharField(max_length=20, default=None)

    class Meta:
        app_label = "gameapp"

    def __unicode__(self):
        return self.username
