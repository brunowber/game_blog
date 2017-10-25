# coding=utf-8

from django.shortcuts import render, redirect
from django.views import View
from gameapp.models.usuario_model import UsuarioModel
from gameapp.forms.usuario_forms import UsuarioForm, UsuarioEditForm


class CadastraUsuario(View):
    template = 'criar_usuario.html'

    def get(self, request, identificador=None):
        """Envia o formulário para a criação ou edição dos usuários"""

        print (identificador)
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
