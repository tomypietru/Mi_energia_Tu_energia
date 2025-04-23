from django.db import models

class Producto(models.Model):
    CATEGORIAS = (
        ('velas', 'Velas'),
        ('perfumes', 'Perfumes'),
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    

    def __str__(self):
        return self.nombre

