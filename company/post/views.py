from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from post.models import *


def blog(request):
    header = 'Welcome to Ehsan Software Blog Page..'
    user_list = Post.objects.filter().order_by('id').reverse()
    category = Category.objects.all()
    tag = Tag.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'data': users, 'header': header, 'categories': category, 'tags': tag})


def postdetails (request, id):
    data = Post.objects.get(pk=id)
    tag = data.tag
    header = 'Blog Details page.'

    return render(request, 'blog/details.html', {'data': data, 'tags': tag, 'header':header })


def post_by_tag(request, id):
    header = "Post By Tags "
    tag = Tag.objects.get(id = id)
    articles = Post.objects.filter(tag=tag)

    return render(request, 'blog/post_by_tag.html', {'instance': articles})


def post_by_cat(request, id):
    header = "Post By Category "
    category = Category.objects.get(id = id)
    articles = Post.objects.filter(category=category)

    return render(request, 'blog/post_by_cat.html', {'instance': articles})