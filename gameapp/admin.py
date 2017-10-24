from django.contrib import admin
from models.usuario_model import UsuarioModel
from models.post_model import PostModel
from models.curtir_model import CurtirModel
from models.comentario_model import ComentarioModel

# Register your models here.
admin.site.register(UsuarioModel)
admin.site.register(ComentarioModel)
admin.site.register(CurtirModel)
admin.site.register(PostModel)
