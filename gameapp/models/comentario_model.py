# coding: utf-8
"""Model de comentários"""

from django.db import models
from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.curtir_model import CurtirModel


class ComentarioModel(models):
    """model de comentários"""

    cutir = models.BooleanField(default=False)

    usuario = models.ForeignKey(UsuarioModel)
    comentario = models.CharField(CurtirModel)
