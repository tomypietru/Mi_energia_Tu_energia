from django.urls import path
from catalogo import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/perfumes', views.perfumes, name='perfumes'),
    path('productos/velas', views.velas, name='velas'),

]