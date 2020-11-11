from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def front_page(request):
    context = {}
    template = loader.get_template("front_page/front_page.html")

    return HttpResponse(template.render(context, request))
