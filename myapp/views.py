from django.shortcuts import render
from django.http import HttpResponse

def data_view(request):
    return HttpResponse("Страница Data")

def test_view(request):
    return HttpResponse("Страница Test")