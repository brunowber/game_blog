# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from gameapp.decorators.autenticado import autenticado
from gameapp.models.usuario_model import UsuarioModel
from gameapp.forms.usuario_forms import UsuarioForm, UsuarioEditForm, LoginForm


class CadastraUsuario(View):
    template = 'criar_usuario.html'

    def get(self, request, identificador=None):
        """Envia o formulário para a criação ou edição dos usuários"""

        if identificador:
            usuario = UsuarioModel.objects.get(pk=identificador)
            form = UsuarioEditForm(instance=usuario)
        else:
            form = UsuarioForm()

        return render(request, self.template, {'form': form})

    def post(self, request, identificador=None):
        """Envia para o banco os usuários criados ou editados"""

        if identificador:
            usuario = UsuarioModel.objects.get(pk=identificador)
            form = UsuarioEditForm(instance=usuario, data=request.POST)
        else:
            form = UsuarioForm(request.POST)
        if form.is_valid():
            form.is_active = True
            form.save()
            return redirect('/')

        return render(request, self.template, {'form': form})


class Login(View):
    template = 'login.html'

    def get(self, request):
        form = LoginForm()

        return render(request, self.template, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print username, password
        try:
            form = LoginForm(data=request.POST, instance=UsuarioModel.objects.get(username=username))
        except ObjectDoesNotExist:
            form = LoginForm(data=request.POST)
        if not form.is_valid():
            print form.errors
            return render(request, self.template, {'form': form})
        username = form.save(commit=False).username
        password = form.save(commit=False).password

        user = authenticate(username=username, password=password)
        print user
        if user:
            login(request, user)
            usuario = LoginForm(data=request.POST, instance=UsuarioModel.objects.get(username=username))

            if usuario.is_valid():
                return redirect('/')
            else:
                print usuario.errors
        else:
            return render(request, self.template, {'form': LoginForm})


class Perfil(View):
    template = "ver_post.html"

    @method_decorator(autenticado())
    def get(self, request):
        jogo = UsuarioModel.objects.get(pk=request.user.id)
        print jogo.jogo
        return render(request, self.template, {'jogo': jogo.jogo})
