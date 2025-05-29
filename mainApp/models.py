from django.db import models
from django.utils.text import slugify

class Eventos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    productora = models.CharField(max_length=50)
    duracion = models.PositiveBigIntegerField()
    imagenes = models.ImageField(upload_to="eventos")
    
    def __str__(self):
        return f"{self.nombre} ({self.descripcion})"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    eventos = models.ManyToManyField(Eventos, related_name='categorias')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Funcion(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.PositiveBigIntegerField()
    asientos_disponibles = models.PositiveBigIntegerField()
    asientos_vendidos = models.PositiveBigIntegerField()
    lugar = models.CharField(max_length=50)

    def __str__(self):
        return self.evento.nombre

class Ubicacion(models.Model):
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    asientos_disponibles = models.PositiveIntegerField()
    asientos_vendidos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"

class Ventas(models.Model):
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    entradas = models.PositiveBigIntegerField()
    total_original = models.PositiveBigIntegerField(default=0)
    total_descuento = models.PositiveBigIntegerField(default=0)
    total_final = models.PositiveBigIntegerField(default=0)
    fecha = models.DateField()




