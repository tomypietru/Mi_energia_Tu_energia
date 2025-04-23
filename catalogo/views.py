from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from .models import Producto

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


def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))  

    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += cantidad
    else:
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': cantidad,
        }

    request.session['carrito'] = carrito
    return redirect(request.META.get('HTTP_REFERER', "/"))  

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())

    total = 0
    detalles = []

    for producto in productos:
        item = carrito[str(producto.id)]
        subtotal = item['precio'] * item['cantidad']
        total += subtotal
        detalles.append({
            'id': producto.id,
            'nombre': item['nombre'],
            'categoria': producto.categoria,
            'precio_unitario': item['precio'],
            'cantidad': item['cantidad'],
            'subtotal': subtotal,
        })

    return render(request, 'catalogo/carrito.html', {
        'carrito_detalles': detalles,
        'total': total,
    })

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
    
    return redirect('ver_carrito')

def perfumes_view(request):
    perfumes = Producto.objects.filter(categoria='perfumes')
    return render(request, "catalogo/productos_templates/perfumes.html", {'productos': perfumes})

def velas_view(request):
    velas = Producto.objects.filter(categoria='velas')
    return render(request,"catalogo/productos_templates/velas.html", {'productos': velas})