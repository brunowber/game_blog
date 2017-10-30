# coding: utf-8
"""Model de curtidas"""

from django.db import models
from gameapp.models import ComentarioModel


class CurtirModel(models.Model):

    coment = models.ForeignKey(ComentarioModel)

    class Meta:
        app_label = "gameapp"
