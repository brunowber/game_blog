from django.shortcuts import render
from gameapp.models.post_model import PostModel


def index(request):
    template = "index.html"

    context_dict = {}
    posts = PostModel.objects.all()
    context_dict['posts'] = posts

    return render(request, template, context_dict)
