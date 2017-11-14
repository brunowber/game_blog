# -*- coding: utf-8 -*-
"""Forms para usuários"""

from __future__ import unicode_literals
from django import forms

from django.utils.translation import ugettext_lazy as _
from gameapp.models.usuario_model import UsuarioModel


class UsuarioForm(forms.ModelForm):
    """Forms para criação de usuários"""
    username = forms.CharField(max_length=254, label='Nome de Usuário')
    first_name = forms.CharField(max_length=40, label='Nome')
    last_name = forms.CharField(max_length=40, label='Sobrenome')
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    jogo = forms.CharField(max_length=40, label='Jogo Preferido')

    class Meta:
        model = UsuarioModel
        fields = "__all__"
        exclude = ['date_joined', 'is_active']

    def save(self, commit=True):
        usuario = super(UsuarioForm, self).save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        if commit:
            usuario.save()
        return usuario


class UsuarioEditForm(forms.ModelForm):
    """Forms para edição de usuários"""
    first_name = forms.CharField(max_length=40, label='Nome')
    last_name = forms.CharField(max_length=40, label='Sobrenome')
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    jogo = forms.CharField(max_length=40, label='Jogo Preferido')

    class Meta:
        model = UsuarioModel
        fields = "__all__"
        exclude = ['date_joined', 'is_active', 'username']

    def save(self, commit=True):
        usuario = super(UsuarioEditForm, self).save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        if commit:
            usuario.save()
        return usuario


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=40, label=_("Usuário"),
                               widget=forms.TextInput(attrs={'placeholder': _('Usuário')}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder': _('Senha')}))

    class Meta:
        model = UsuarioModel
        fields = ['username', 'password']

