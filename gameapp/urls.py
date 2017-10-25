from django.conf.urls import url

from gameapp.views.usuario_view import CadastraUsuario
from gameapp.views.post_view import CadastraPost, CadastraComentario


urlpatterns = [
    url(r'^cad_usuario/$', CadastraUsuario.as_view(), name='cadastro-usuario'),
    url(r'^edita_usuario/(?P<identificador>\d+)/$', CadastraUsuario.as_view(), name='edita-usuario'),

    url(r'^cad_post/$', CadastraPost.as_view(), name='cria-post'),
    url(r'^edita_post/(?P<identificador>\d+)/$', CadastraPost.as_view(), name='edita-post'),

    url(r'^cad_comentario/(?P<identificador>\d+)/$', CadastraComentario.as_view(), name='cria-comentario'),
    url(r'^edita_comentario/(?P<identificador>\w+)/$', CadastraComentario.as_view(), name='edita-comentario'),
]
