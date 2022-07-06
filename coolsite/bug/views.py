from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'О сайте', 'url_name':'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    posts = Bug.objects.all()
    return render(request, 'bug/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная странциа'})

def about(request):
    return render(request, 'bug/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive (request,year):
    if int(year) > 2022:
        return redirect('home')

    return HttpResponse(f'<h1>Архив по играм</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
