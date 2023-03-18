from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_list(request, slug):
    return HttpResponse(f'Список постов {slug}')