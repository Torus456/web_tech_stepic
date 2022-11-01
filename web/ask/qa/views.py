from django.shortcuts import render

from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def step2_1(request):
    return HttpResponse('OK')

def error404(request):
    return HttpResponse('OK')
