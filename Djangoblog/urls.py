# -*- coding: utf-8 -*-
"""Djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog.views import index,django,python,linux,network,football,javascript

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name="index"),  #首页映射
    url(r'^django/$',django,name="django"),     #django映射
    url(r'^python/$',python,name="python"),      #python映射
    url(r'^linux/$',linux,name="linux"),
    url(r'^network/$',network,name="network"),
    url(r'^football/$',football,name="football"),
    url(r'^javascript/$',javascript,name="javascript"),
]
