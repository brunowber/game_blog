# coding=utf-8

from django import forms
from gameapp.models.post_model import PostModel


class PostForm(forms.ModelForm):
    titulo = forms.CharField(max_length=30, label='Título')
    texto = forms.CharField(max_length=200, label='Texto')

    class Meta:
        model = PostModel
        fields = "__all__"
        exclude = ['curtir', 'usuario']
