from django.shortcuts import render

# Create your views here.
def cronometro(request):
    return render(request, 'cronometro/cronometro.html')