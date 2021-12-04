from django.shortcuts import render
from django.http import HttpResponse

from retroCar.models import Post
from .models import *

menu = [{'title': "О сайте", 'url_name': 'categories'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Post.objects.all()
    cats = Category.objects.all()

    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0,
               }
    return render(request, 'retroCar/index.html', context=context)


def categories(request):
    return render(request, "retroCar/categories.html", {'menu': menu, 'title': 'Cтраница категорий'})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return render(request, 'retroCar/login.html')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()



    context = {'posts': posts,
               'cats': cats,
               'menu': menu,
               'title': 'Отображение по рубрикам',
               'cat_selected': cat_id,
               }
    return render(request, 'retroCar/index.html', context=context)
