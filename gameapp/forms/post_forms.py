# -*- coding: utf-8 -*-
"""Forms para os posts"""
from django import forms
from gameapp.models.post_model import PostModel


class PostForm(forms.ModelForm):
    """Form de criação de posts"""
    titulo = forms.CharField(max_length=30, label='Título')
    texto = forms.CharField(max_length=1000, label='Texto',
                            widget=forms.Textarea)

    class Meta:
        model = PostModel
        fields = "__all__"
        exclude = ['curtir', 'usuario', 'curtidas']

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        if commit:
            post.save()
        return post


class PostEditForm(forms.ModelForm):
    """Forms para edição de posts"""
    titulo = forms.CharField(max_length=30, label='Título')
    texto = forms.CharField(max_length=300, label='Texto')

    class Meta:
        model = PostModel
        fields = "__all__"
        exclude = ['curtir', 'usuario', 'curtidas']

    def save(self, commit=True):
        post = super(PostEditForm, self).save(commit=False)
        if commit:
            post.save()
        return post
