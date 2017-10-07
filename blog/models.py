# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    item = models.CharField(verbose_name="类别",max_length=50)
    desc = models.CharField(verbose_name="描述",max_length=50)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.item

class Django(models.Model):
    title = models.CharField(verbose_name="标题",max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category,verbose_name="类别")

    class Meta:
        verbose_name = "Django"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Python(models.Model):
    title = models.CharField(verbose_name="标题",max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category,verbose_name="类别")

    class Meta:
        verbose_name = "Python"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Linux(models.Model):
    title = models.CharField(verbose_name="标题",max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category,verbose_name="类别")

    class Meta:
        verbose_name = "Linux"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Network(models.Model):
    title = models.CharField(verbose_name="标题",max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category,verbose_name="类别")

    class Meta:
        verbose_name = "Network"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Football(models.Model):
    title = models.CharField(verbose_name="标题",max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category,verbose_name="类别")

    class Meta:
        verbose_name = "Football"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

class Javascript(models.Model):
    title = models.CharField(verbose_name="标题",max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category,verbose_name="类别")

    class Meta:
        verbose_name = "Javascript"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title