from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.

class Testimonios(models.Model):
    testimonio = models.TextField()
    nombre = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='perfil', help_text='Perfil con formato cuadrangular', default='perfil/default.png')

    estado = models.BooleanField(default=True) #estado del usuario activo o no
    creado = models.DateTimeField(auto_now_add=True) #fecha de creación del usuario
    actualizado = models.DateTimeField(auto_now_add=True) #fecha actualizado de datos

    def __str__(self):
        return self.nombre


class Clientes(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField( null=True, blank=True)
    logotipo = models.ImageField(upload_to='logotipos', help_text='Logotipo con formato rectangular', default='logotipos/default.png')
    url = models.URLField()
    estado = models.BooleanField(default=True) #estado del usuario activo o no
    creado = models.DateTimeField(auto_now_add=True) #fecha de creación del usuario
    actualizado = models.DateTimeField(auto_now_add=True) #fecha actualizado de datos

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=85, blank=True)

    def save(self, *args, **kwargs): #creacion de slug automático
        self.slug = slugify(self.nombre)
        super(Tipo, self).save(*args, **kwargs)


    estado = models.BooleanField(default=True) #estado del usuario activo o no
    creado = models.DateTimeField(auto_now_add=True) #fecha de creación del usuario
    actualizado = models.DateTimeField(auto_now_add=True) #fecha actualizado de datos

    def __str__(self):
        return self.nombre

class Proyectos(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField( null=True, blank=True)
    imagen = models.ImageField(upload_to='logotipos', help_text='Logotipo con formato rectangular', default='logotipos/default.png')
    url = models.URLField()
    estado = models.BooleanField(default=True) #estado del usuario activo o no
    creado = models.DateTimeField(auto_now_add=True) #fecha de creación del usuario
    actualizado = models.DateTimeField(auto_now_add=True) #fecha actualizado de datos

    def __str__(self):
        return self.nombre


class Contactos(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.PositiveIntegerField()
    email =  models.EmailField()
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()

    estado = models.BooleanField(default=True) #estado del usuario activo o no
    creado = models.DateTimeField(auto_now_add=True) #fecha de creación del usuario
    actualizado = models.DateTimeField(auto_now_add=True) #fecha actualizado de datos

    def __str__(self):
        return self.nombre