# coding: utf8
from django.shortcuts import render, render_to_response
from django.template import RequestContext


def home(request, template_name="core/home.html"):
  return render_to_response(template_name, locals(), context_instance=RequestContext(request))
