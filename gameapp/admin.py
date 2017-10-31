# -*- coding: utf-8 -*-
"""Página da administração do Django"""

from django.contrib import admin
from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.post_model import PostModel
from gameapp.models.curtir_model import CurtirModel
from gameapp.models.comentario_model import ComentarioModel

admin.site.register(UsuarioModel)
admin.site.register(ComentarioModel)
admin.site.register(CurtirModel)
admin.site.register(PostModel)
