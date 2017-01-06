# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Ambiente
from .models import RepositorioDados

admin.site.register(Ambiente)
admin.site.register(RepositorioDados)
