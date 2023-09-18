from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, stock_id):
    return HttpResponse(f'This is the detail view for stock {stock_id}')
