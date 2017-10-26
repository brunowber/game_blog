from django.shortcuts import render_to_response, render
from django.template import RequestContext


def index(request):
    template = "index.html"
    # return render_to_response("index.html", RequestContext(request))
    return render(request, template)
