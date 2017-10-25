# coding=utf-8

from django.shortcuts import render, redirect
from django.views import View
from gameapp.models.post_model import PostModel
from gameapp.models.usuario_model import UsuarioModel
from gameapp.models.comentario_model import ComentarioModel
from gameapp.forms.post_forms import PostForm, PostEditForm
from gameapp.forms.comentario_forms import ComentarioForm, ComentarioEditForm


class CadastraPost(View):
    template = 'criar_post.html'

    def get(self, request, identificador=None):
        """Envia o formulário para a criação ou edição dos Posts"""

        if identificador:
            post = PostModel.objects.get(pk=identificador)
            form = PostEditForm(instance=post)
        else:
            form = PostForm()

        return render(request, self.template, {'form': form})

    def post(self, request, identificador=None):
        """Envia para o banco os Posts criados ou editados"""

        usuario = request.user.id
        if identificador:
            post = PostModel.objects.get(pk=identificador)
            form = PostEditForm(instance=post, data=request.POST)
        else:
            form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = UsuarioModel.objects.get(pk=usuario)
            post.save()
            return redirect('/')

        return render(request, self.template, {'form': form})


class CadastraComentario(View):
    template = 'criar_comentario.html'

    def get(self, request, identificador=None):
        """Envia o formulário para a criação ou edição dos Comentarios"""

        form = ComentarioForm()

        return render(request, self.template, {'form': form})

    def post(self, request, identificador=None):
        """Envia para o banco os Comentarios criados ou editados"""

        usuario = request.user.id
        #if identificador:
         #   print "aqui"
          #  comentario = ComentarioModel.objects.get(pk=identificador)
           # form = ComentarioEditForm(instance=comentario, data=request.POST)
        #else:
        form = ComentarioForm(request.POST)
        print form
        print "form comentario", form.is_valid()
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = UsuarioModel.objects.get(pk=2)
            comentario.post = PostModel.objects.get(pk=identificador)
            comentario.like = 0
            comentario.save()
            return redirect('/')

        return render(request, self.template, {'form': form})