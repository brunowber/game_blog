# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from gameapp.decorators.autenticado import autenticado
from gameapp.models.post_model import PostModel
from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.comentario_model import ComentarioModel
from gameapp.models.curtir_model import CurtirModel
from gameapp.forms.post_forms import PostForm, PostEditForm
from gameapp.forms.comentario_forms import ComentarioForm


class CadastraPost(View):
    template = 'postagem.html'

    @method_decorator(autenticado())
    def get(self, request, identificador=None):
        """Envia o formulário para a criação ou edição dos Posts"""

        if identificador:
            post = PostModel.objects.get(pk=identificador)
            form = PostEditForm(instance=post)
        else:
            form = PostForm()

        return render(request, self.template, {'form': form})

    @method_decorator(autenticado())
    def post(self, request, identificador=None):
        """Envia para o banco os Posts criados ou editados"""
        user = UsuarioModel.objects.get(pk=request.user.id)
        if identificador:
            post = PostModel.objects.get(pk=identificador)
            form = PostEditForm(instance=post, data=request.POST)
        else:
            form = PostForm(request.POST)
        print form.is_valid(), form
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = UsuarioModel.objects.get(pk=user)
            print post
            post.save()
            return redirect('/')

        return render(request, self.template, {'form': form})


class CadastraComentario(View):
    template = 'criar_comentario.html'

    @method_decorator(autenticado())
    def get(self, request, identificador=None):
        """Envia o formulário para a criação ou edição dos Comentarios"""

        form = ComentarioForm()

        return render(request, self.template, {'form': form})

    @method_decorator(autenticado())
    def post(self, request, identificador=None):
        """Envia para o banco os Comentarios criados ou editados"""

        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = UsuarioModel.objects.get(pk=2)
            comentario.post = PostModel.objects.get(pk=identificador)
            comentario.like = 0
            comentario.save()
            return redirect('/')

        return render(request, self.template, {'form': form})


class VerPost(View):
    template = 'ver_post.html'

    def get(self, request, identificador=None):
        context_dict = {}
        post = PostModel.objects.get(pk=identificador)
        context_dict['post'] = post
        comentarios = ComentarioModel.objects.filter(post=identificador)
        context_dict['comentarios'] = comentarios
        form = ComentarioForm()
        context_dict['comentar'] = form

        return render(request, self.template, context_dict, {'form': form})

    @method_decorator(autenticado())
    def post(self, request, identificador=None):
        print identificador
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = UsuarioModel.objects.get(pk=request.user.id)
            comentario.post = PostModel.objects.get(pk=identificador)
            comentario.like = 0
            comentario.save()

            return redirect("/ver_post/%d" % comentario.post_id)


class Like(View):
    @method_decorator(autenticado())
    def post(self, request, identificador=None):
        user = UsuarioModel.objects.get(pk=request.user.id)
        comentario = ComentarioModel.objects.get(pk=identificador)
        curtidas = CurtirModel.objects.filter(usuario=user, coment=comentario)
        if curtidas.count() == 0:
            comentario.like += 1
            comentario.save()
            curtida = CurtirModel.objects.create(usuario=user, coment=comentario)
            curtida.save()
        else:
            comentario.like -= 1
            comentario.save()
            curtida = CurtirModel.objects.get(usuario=user, coment=comentario)
            curtida.delete()

        return redirect("/ver_post/%d" % comentario.post_id)


class LikePost(View):
    template = 'ver_post.html'

    @method_decorator(autenticado())
    def post(self, request, identificador=None):
        user = UsuarioModel.objects.get(pk=request.user.id)
        post = PostModel.objects.get(pk=identificador)
        curtidas = CurtirModel.objects.filter(usuario=user, post=post)
        if curtidas.count() == 0:
            post.curtidas += 1
            post.save()
            curtida = CurtirModel.objects.create(usuario=user, post=post)
            curtida.save()
        else:
            post.curtidas -= 1
            post.save()
            curtida = CurtirModel.objects.get(usuario=user, post=post)
            curtida.delete()

        return redirect("/ver_post/%d" % int(identificador))


class PostagemListarViews(ListView):
    """Classe genérica de view de listagem dos posts"""

    template_name = 'todas_postagens.html'

    def get_queryset(self):
        """Método de definição de queryset"""
        return PostModel.objects.all().order_by('-pk')
