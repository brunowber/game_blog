# -*- coding: utf-8 -*-
"""Configurações das Urls"""
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from gameapp import views

from gameapp.views.usuario_view import CadastraUsuario, Login, Perfil
from gameapp.views.post_view import CadastraPost, CadastraComentario,\
    VerPost, Like, LikePost, PostagemListarViews


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postagens/$', PostagemListarViews.as_view(), name='postagens'),
    url(r'^cad_usuario/$', CadastraUsuario.as_view(), name='cadastro-usuario'),
    url(r'^edita_usuario/(?P<identificador>\d+)/$', CadastraUsuario.as_view(),
        name='edita-usuario'),

    url(r'^cad_post/$', CadastraPost.as_view(), name='cria-post'),
    url(r'^edita_post/(?P<identificador>\d+)/$', CadastraPost.as_view(),
        name='edita-post'),

    url(r'^cad_comentario/(?P<identificador>\d+)/$', CadastraComentario.as_view(),
        name='cria-comentario'),
    url(r'^edita_comentario/(?P<identificador>\w+)/$',
        CadastraComentario.as_view(), name='edita-comentario'),

    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'},
        name='logout'),

    url(r'^perfil/$', Perfil.as_view(), name='perfil-usuario'),

    url(r'^criar_post/$', CadastraPost.as_view(), name='criar-post'),
    url(r'^criar_post/(?P<identificador>\d+)/$', CadastraPost.as_view(),
        name='criar-post'),

    url(r'^ver_post/(?P<identificador>\d+)/$', VerPost.as_view(),
        name='ver-post'),
    url(r'^ver_post/(?P<identificador>\d+)/$', VerPost.as_view(),
        name='cadastrar-comentario'),

    url(r'^curtir/(?P<identificador>\d+)/$', Like.as_view(),
        name='curtir-comentario'),
    url(r'^curtir_post/(?P<identificador>\d+)/$', LikePost.as_view(),
        name='curtir-post'),
]
