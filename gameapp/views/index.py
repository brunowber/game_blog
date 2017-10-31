# -*- coding: utf-8 -*-
"""View de index"""
from django.shortcuts import render
from gameapp.models.post_model import PostModel


def index(request):
    """View para chamar a página principal"""
    template = "index.html"

    context_dict = {}
    posts = PostModel.objects.all()
    posts = posts.order_by('-pk')[:20]
    context_dict['posts'] = posts

    return render(request, template, context_dict)
