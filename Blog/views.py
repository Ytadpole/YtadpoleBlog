# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from Blog.Form import CommentForm
from Blog.models import Blog, Comment


def get_blogs(request):
    ctx = {
        'blogs':Blog.objects.all().order_by('-createdTime')
    }
    return render(request, 'blog-list.html', ctx)

def get_detail(request , blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method =='GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx ={
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-createTime'),
        'form':form
    }
    return render(request,'blog_detail.html', ctx)

def aboutMe(request):
    return render(request, "about.html")