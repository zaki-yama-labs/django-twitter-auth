# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    context = RequestContext(request,
                             {'user': request.user})
    return render_to_response('app/home.html',
                              context_instance=context)
