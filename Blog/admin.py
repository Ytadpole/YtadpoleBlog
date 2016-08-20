# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from Blog.models import Blog,Category,Tag

admin.site.register([Category, Tag, Blog])