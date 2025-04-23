from django.urls import path
from catalogo import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('perfumes/', views.perfumes_view, name='perfumes'),
    path('productos/velas', views.velas_view, name='velas'),
    path('carrito/ver/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),



]