# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Django,Python,Linux,Network,Football,Javascript

# Create your views here.
def index(request):
    return render(request,"index.html",{})  #首页视图函数

def django(request):
    all_django = Django.objects.all()
    return render(request,"django.html",{
        "all_django":all_django,
    })                                           #django视图函数

def python(request):
    all_python = Python.objects.all()
    return render(request,"python.html",{
        "all_python":all_python,
    })                                            #python视图函数

def linux(request):
    all_linux = Linux.objects.all()
    return render(request,"linux.html",{
        "all_linux":all_linux,
    })      #linux视图函数

def network(request):
    all_network = Network.objects.all()
    return render(request, "network.html",{
        "all_network":all_network,
    })      #html视图函数

def football(request):
    all_football = Football.objects.all()
    return  render(request,"football.html",{
        "all_footballl":all_football,
    })      #football视图函数

def javascript(request):
    all_javascript = Javascript.objects.all()
    return render(request,"javascript.html",{
        "all_javascript":all_javascript,
    })     #js视图函数