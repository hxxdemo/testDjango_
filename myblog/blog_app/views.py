from django.shortcuts import render,redirect

from .models import Article

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    context = {}
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Article.objects.filter(tag=queryset)
        #article_list = mypaginator(article_list)
    else:
        article_list = Article.objects.all()
        #article_list = mypaginator(article_list)
    context['article_list'] = article_list
    return render(request, 'index.html', context)


def detail(request, id):
    context = {}
    article_id = Article.objects.get(id=id)
    context = {
        'article_id': article_id
    }
    return render(request, 'detail.html',context)


def mypaginator(articles):
    pager = Paginator(articles,5)
    page_num = request.GET.get('page', 1)
    try:
        a_list = pager.page(page_num)
    except EmptyPage:
        a_list = pager.page(pager.num_pages)
    except PageNotAnInteger:
        a_list = pager.page(1)
    return a_list