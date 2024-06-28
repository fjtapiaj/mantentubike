from django.http import HttpResponse
from django.shortcuts import render

def cronometro(request):
    return render(request, 'cronometro.html')


def bienvenida (request):
    return HttpResponse("bienvenido a manten tu bike")