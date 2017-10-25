# coding=utf-8

from django import forms
from gameapp.models.usuario_model import UsuarioModel


class ClienteForm(forms.ModelForm):
    username = forms.CharField(max_length=254, label='Nome de Usuário')
    first_name = forms.CharField(max_length=40, label='Nome')
    last_name = forms.CharField(max_length=40, label='Sobrenome')
    password = forms.CharField(widget=forms.PasswordInput())
    jogo = forms.CharField(max_length=40, label='Jogo Preferido')

    class Meta:
        model = UsuarioModel
        fields = "__all__"
        exclude = ['date_joined', 'is_active']
