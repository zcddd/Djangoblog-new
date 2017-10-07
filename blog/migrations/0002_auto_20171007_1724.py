# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
            ],
            options={
                'verbose_name': 'Football',
                'verbose_name_plural': 'Football',
            },
        ),
        migrations.CreateModel(
            name='Javascript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
            ],
            options={
                'verbose_name': 'Javascript',
                'verbose_name_plural': 'Javascript',
            },
        ),
        migrations.CreateModel(
            name='Linux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
            ],
            options={
                'verbose_name': 'Linux',
                'verbose_name_plural': 'Linux',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
            ],
            options={
                'verbose_name': 'Network',
                'verbose_name_plural': 'Network',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u7c7b\u522b', 'verbose_name_plural': '\u7c7b\u522b'},
        ),
        migrations.AlterModelOptions(
            name='django',
            options={'verbose_name': 'Django', 'verbose_name_plural': 'Django'},
        ),
        migrations.AlterModelOptions(
            name='python',
            options={'verbose_name': 'Python', 'verbose_name_plural': 'Python'},
        ),
        migrations.AddField(
            model_name='network',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='linux',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='javascript',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='football',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='\u7c7b\u522b'),
        ),
    ]
