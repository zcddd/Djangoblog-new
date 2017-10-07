# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Category,Django,Python,Linux,Network,Football,Javascript
# Register your models here.

class  CategoryAdmin(admin.ModelAdmin):
    pass

class DjangoAdmin(admin.ModelAdmin):
    pass

class PythonAdmin(admin.ModelAdmin):
    pass

class LinuxAdmin(admin.ModelAdmin):
    pass

class Networkadmin(admin.ModelAdmin):
    pass

class FootballAdmin(admin.ModelAdmin):
    pass

class JavascriptAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)
admin.site.register(Django,DjangoAdmin)
admin.site.register(Python,PythonAdmin)
admin.site.register(Linux,LinuxAdmin)
admin.site.register(Network,Networkadmin)
admin.site.register(Football,FootballAdmin)
admin.site.register(Javascript,JavascriptAdmin)