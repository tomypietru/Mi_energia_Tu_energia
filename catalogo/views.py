from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'catalogo/index.html')

def contacto(request):
    return render(request, "catalogo/contacto.html")

def nosotros(request):
    return render(request, "catalogo/nosotros.html")

def perfumes(request):
    return render(request, "catalogo/productos_templates/perfumes.html")

def velas(request):
    return render(request, "catalogo/productos_templates/velas.html")