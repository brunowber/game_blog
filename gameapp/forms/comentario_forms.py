# coding=utf-8

from django import forms
from gameapp.models.comentario_model import ComentarioModel


class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(max_length=1000, label='Comentario', widget=forms.Textarea)

    class Meta:
        model = ComentarioModel
        fields = ["comentario"]

    def save(self, commit=True):
        comentario = super(ComentarioForm, self).save(commit=False)
        if commit:
            comentario.save()
        return comentario


class ComentarioEditForm(forms.ModelForm):
    comentario = forms.CharField(max_length=1000, label='Texto', widget=forms.Textarea)

    class Meta:
        model = ComentarioModel
        fields = ["comentario"]

    def save(self, commit=True):
        comentario = super(ComentarioEditForm, self).save(commit=False)
        if commit:
            comentario.save()
        return comentario
