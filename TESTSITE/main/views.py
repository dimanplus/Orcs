from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q

from .forms import *
from .models import *

# Create your views here.

menu = [{'title': "Главная", 'url_name':'home'},
        {'title': 'Список Орков', 'url_name': 'orki'},
        {'title':'Добавить Орков', 'url_name':'add_ork'},
        {'title':'Удалить Орков', 'url_name':'rem_ork'},
#        {'title':'Корзина', 'url_name':'card'}
]

add_button = ['В корзину']


# def index(request):
#     return render(request, 'main/index.html', {'menu': menu, 'title': 'Главная'})

def index(request):
    q = request.GET.get("q")
    if q:
        q_list = q.split(' ')
        # print(type(q_list))
        # print(q_list)
        orcs = Orc.objects.filter(
            Q(title__in=q_list) | Q(content__in=q_list) |
            Q(title__icontains=q) | Q(content__icontains=q) |
            Q(der__title__in=q_list)
        )
        # derev = Der.objects.filter(
        #     Q(title__in=q_list) | Q(der__title__in=q_list)|
        #     Q(title__icontains=q) | Q(der__title__icontains=q)
        # )
        # print(orcs)
        # print(derev)
    else:
        orcs = None
        # derev = None
    return render(request, 'main/index.html', {'orc_list': orcs, 'menu': menu, 'title': 'Главная'})

def orki(request):
    posts = Orc.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title':'Список Орков'
    }
    return render (request, 'main/orki.html', context = context)

def add_ork(request):
    posts = Orc.objects.all()
    context = {
    'posts': posts,
    'menu': menu,
    'title': 'Редактировать Орков'
    }
    if request.method == 'POST':
        form = AddOrkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_ork')
    else:
        form = AddOrkForm()
    context['form'] = form
    return render(request, 'main/add_ork.html', context)

def rem_ork(request):
    posts = Orc.objects.all()
    context = {
    'posts': posts,
    'menu': menu,
    'title': 'Редактировать Орков'
    }
    if request.method == 'POST':
        form = RemOrkForm(request.POST)
        if form.is_valid():
            ork_title = form.cleaned_data['title']
            Orc.objects.filter(title=ork_title).delete()
            return redirect('rem_ork')
    else:
        form = RemOrkForm()
    context['form'] = form
    return render(request, 'main/rem_ork.html', context)


def card(request):
    return render (request, 'main/card.html', {'menu': menu, 'title':'Корзина'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Данной страницы не существует</h2>')
