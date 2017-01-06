# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Ambiente

def index(request):
    latest_ambiente_list = Ambiente.objects.order_by('tipo')[:5]
    template = loader.get_template('ETL/index.html')
    context = {'latest_ambiente_list': latest_ambiente_list}
    return HttpResponse(template.render(context, request))


def detail(request, ambiente_id):
	return HttpResponse("This is the %s Ambient." % ambiente_id)
