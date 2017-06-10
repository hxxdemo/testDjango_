from django.shortcuts import render,redirect

from .form import LoginForm, RegisterForm, EditForm
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    '''
    首页
    '''
    context = {}
    cates = Category.objects.all().order_by('-id')

    big_today_news = Best.objects.filter(select_reason='今日新闻')[0].select_article
    small_today_news_list = Best.objects.filter(select_reason='今日新闻')[1:5]
    small_today_news = [i.select_article for i in small_today_news]

    index_intro_list = Best.objects.filter(select_reason='首页推荐')[0:3]
    index_intros = [i.select_article for i in index_intro_list]

    big_editor_list = Best.objects.filter(select_reason='编辑推荐')[0:3]
    big_editors = [i.select_article for i in big_editor_list]
    small_editor_list = Best.objects.filter(select_reason='编辑推荐')[3:9]
    small_editors = [i.select_article for i in small_editor_list]

    article_list = Article.objects.all().order_by('-publish_time')
    pager = Paginator(article_list, 6)
    page_num = request.GET.get('page', 1)
    try:
        article_list = pager.page(page_num)
    except:
        article_list = pager.page(num_pages)
    except:
        article_list = pager.page(1)
    context = {
        'cates': cates,
        'big_today_news': big_today_news,
        'small_today_news': small_today_news,
        'index_intro': index_intros,
        'big_editor': big_editors,
        'small_editor': small_editors,
        'article_list': article_list
    }
    return render(request, 'index.html', context=context)


def category(request, cate_id):
    context = {}
    return render(request, 'categories.html', context=context)


def detail(request, article_id):
    context = {}

    if request.GET.get('abstract', 1) == 1:  # 默认显示摘要
        return render(request, 'detail-abstract.html', context=context)
    else:  # 不显示摘要
        return render(request, 'detail-noabstract.html', context=context)


def login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.clean_data.get('username')
            password = form.clean_data.get('password')
            user = authenicate(username=username,password=password)
            if user:
                django_login(request, user)
                return redirect('index')
        else:
            form.add_error(None, '用户信息错误')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'login.html', con
        text=context)


def register(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = forms.clean_data.get('username')
            email = forms.clean_data.get('email')
            password = form.clean_date.get('password')
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email)
    else:
        form = RegisterForm()
    context['form'] = form
    return render(request, 'regester.html', context=context)


def edit(request):
    context = {}
    user = request.user #找到这个用户
    if request.method == 'POST':
        
        form = EditForm(request.POST)
        if form.is_valid():
            username = form.clean_data.get('username')
            email = form.clean_data.get('email')
            password = form.clean_data.get('password')
            avatar = form.clean_data.get('avatar')
            user.username = username
            user.email = email
            if password:
                user.set_password(password)
            user.save()
            if avatar:
                try:
                    user_profile = UserProfile.objects.get(belong_to=user)
                except ObjectDoesNotExist:
                    user_profile = UserProfile(belong_to=user)
                user_profile.avatar = avatar 
                user_profile.save()
            return redirect('login')
    else:
        # user =request.user
        form = EditForm(initial={
            'username': user.username,
            'email': user.email
            })
    context['form'] = form
    return render(request, 'edit.html', context=context)

