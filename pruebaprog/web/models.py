from django.db import models

# Create your models here.

class Obras(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="obras", null=False)

    def __str__(self):
        return self.nombre


opciones_consulta = [
    (0,'Consulta'),
    (1,'Sugerencia'),
    (2,'Felicitaciones')
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre