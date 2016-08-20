# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('名称', max_length=16)


class Tag(models.Model):
    name = models.CharField('名称', max_length=16)


class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    createdTime = models.DateTimeField('发布时间', auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=140)
    createTime = models.DateTimeField('发布时间', auto_now_add=True)
