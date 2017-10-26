from gameapp import views

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from gameapp.views.usuario_view import CadastraUsuario, Login, Perfil
from gameapp.views.post_view import CadastraPost, CadastraComentario


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cad_usuario/$', CadastraUsuario.as_view(), name='cadastro-usuario'),
    url(r'^edita_usuario/(?P<identificador>\d+)/$', CadastraUsuario.as_view(), name='edita-usuario'),

    url(r'^cad_post/$', CadastraPost.as_view(), name='cria-post'),
    url(r'^edita_post/(?P<identificador>\d+)/$', CadastraPost.as_view(), name='edita-post'),

    url(r'^cad_comentario/(?P<identificador>\d+)/$', CadastraComentario.as_view(), name='cria-comentario'),
    url(r'^edita_comentario/(?P<identificador>\w+)/$', CadastraComentario.as_view(), name='edita-comentario'),

    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'base.html'}, name='logout'),

    url(r'^perfil/$', Perfil.as_view(), name='perfil-usuario'),
]
