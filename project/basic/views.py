from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import gettext as _
from django.utils.translation import activate, get_supported_language_variant


class Index(View):
    def get(self, request):
        string = _('Hello world')
        context = {
            'string' : string
        }
        return HttpResponse(render(request, 'index.html', context))
